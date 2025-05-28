import os
import asyncio
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from database.connection import DatabaseManager
from scrapers.indeed_scraper import IndeedScraper
from ai_matching.matcher import AIJobMatcher
from email_service import EmailService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Job Recruiter Platform",
    description="Automated job matching and recruitment platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global instances
db_manager = None
scraper = None
matcher = None
email_service = None

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    global db_manager, scraper, matcher, email_service
    
    try:
        # Initialize database
        db_manager = DatabaseManager()
        await db_manager.connect()
        logger.info("Database connected successfully")
        
        # Initialize services
        scraper = IndeedScraper()
        matcher = AIJobMatcher()
        email_service = EmailService()
        
        logger.info("All services initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    global db_manager
    if db_manager:
        await db_manager.close()
        logger.info("Database connection closed")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "AI Job Recruiter Platform API",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        # Check database connection
        db_status = "connected" if db_manager and db_manager.client else "disconnected"
        
        return {
            "status": "healthy",
            "database": db_status,
            "services": {
                "scraper": "ready" if scraper else "not_initialized",
                "matcher": "ready" if matcher else "not_initialized",
                "email": "ready" if email_service else "not_initialized"
            },
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/scrape-jobs")
async def scrape_jobs(query: str = "software engineer", location: str = "India", max_jobs: int = 10):
    """Scrape jobs from Indeed"""
    try:
        if not scraper:
            raise HTTPException(status_code=500, detail="Scraper not initialized")
        
        logger.info(f"Starting job scraping: {query} in {location}")
        jobs = await asyncio.to_thread(scraper.scrape_jobs, query, location, max_jobs)
        
        # Save jobs to database
        if db_manager:
            for job in jobs:
                await db_manager.save_job_listing(job)
        
        logger.info(f"Scraped and saved {len(jobs)} jobs")
        return {
            "message": f"Successfully scraped {len(jobs)} jobs",
            "jobs": jobs,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Job scraping failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/find-matches")
async def find_matches():
    """Find matches between candidates and jobs"""
    try:
        if not matcher or not db_manager:
            raise HTTPException(status_code=500, detail="Services not initialized")
        
        logger.info("Starting job matching process")
        
        # Get candidates and jobs from database
        candidates = await db_manager.get_bench_candidates()
        jobs = await db_manager.get_open_jobs()
        
        if not candidates:
            return {
                "message": "No bench candidates found",
                "matches": [],
                "timestamp": datetime.now().isoformat()
            }
        
        if not jobs:
            return {
                "message": "No open jobs found",
                "matches": [],
                "timestamp": datetime.now().isoformat()
            }
        
        # Find matches
        matches = matcher.find_matches(candidates, jobs)
        
        # Save matches to database
        for match in matches:
            await db_manager.save_match_result(match)
        
        logger.info(f"Found {len(matches)} matches")
        return {
            "message": f"Found {len(matches)} matches",
            "matches": matches,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Job matching failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/send-notifications")
async def send_notifications():
    """Send email notifications for matches"""
    try:
        if not email_service or not db_manager:
            raise HTTPException(status_code=500, detail="Services not initialized")
        
        logger.info("Starting email notification process")
        
        # Get recent matches
        matches = await db_manager.get_recent_matches()
        
        if not matches:
            return {
                "message": "No recent matches found",
                "sent": 0,
                "timestamp": datetime.now().isoformat()
            }
        
        sent_count = 0
        for match in matches:
            try:
                success = email_service.send_match_notification(match)
                if success:
                    sent_count += 1
                    # Mark as notified
                    await db_manager.mark_match_notified(match['_id'])
            except Exception as e:
                logger.error(f"Failed to send notification for match {match.get('_id')}: {e}")
        
        logger.info(f"Sent {sent_count} email notifications")
        return {
            "message": f"Sent {sent_count} email notifications",
            "sent": sent_count,
            "total_matches": len(matches),
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Email notification failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-full-cycle")
async def run_full_cycle(
    query: str = "software engineer", 
    location: str = "India", 
    max_jobs: int = 10
):
    """Run complete job matching cycle"""
    try:
        logger.info("Starting full job matching cycle")
        
        # Step 1: Scrape jobs
        scrape_result = await scrape_jobs(query, location, max_jobs)
        
        # Step 2: Find matches
        match_result = await find_matches()
        
        # Step 3: Send notifications
        notification_result = await send_notifications()
        
        return {
            "message": "Full cycle completed successfully",
            "results": {
                "scraping": scrape_result,
                "matching": match_result,
                "notifications": notification_result
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Full cycle failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats():
    """Get platform statistics"""
    try:
        if not db_manager:
            raise HTTPException(status_code=500, detail="Database not initialized")
        
        stats = await db_manager.get_platform_stats()
        return {
            "stats": stats,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = "0.0.0.0"
    
    logger.info(f"Starting server on {host}:{port}")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    ) 