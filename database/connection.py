import os
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import urllib.parse

from database.models import (
    JobListing, CandidateProfile, BenchCandidate, 
    OpenJob, MatchResult, EmailNotification
)

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self.client = None
        self.db = None
        self.connection_string = self._get_connection_string()
    
    def _get_connection_string(self) -> str:
        """Get MongoDB connection string from environment"""
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable not set")
        return mongodb_uri
    
    async def connect(self):
        """Connect to MongoDB"""
        try:
            self.client = AsyncIOMotorClient(self.connection_string)
            # Test connection
            await self.client.admin.command('ping')
            self.db = self.client.airecruiter
            logger.info("Successfully connected to MongoDB")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def close(self):
        """Close MongoDB connection"""
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
    
    async def save_job_listing(self, job_data: Dict[str, Any]) -> str:
        """Save job listing to database"""
        try:
            job_listing = JobListing(**job_data)
            result = await self.db.job_listings.insert_one(job_listing.model_dump())
            logger.info(f"Saved job listing: {job_listing.title} at {job_listing.company}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving job listing: {e}")
            raise
    
    async def save_candidate_profile(self, candidate_data: Dict[str, Any]) -> str:
        """Save candidate profile to database"""
        try:
            candidate = CandidateProfile(**candidate_data)
            result = await self.db.candidate_profiles.insert_one(candidate.model_dump())
            logger.info(f"Saved candidate profile: {candidate.name}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving candidate profile: {e}")
            raise
    
    async def save_bench_candidate(self, candidate_data: Dict[str, Any]) -> str:
        """Save bench candidate to database"""
        try:
            candidate = BenchCandidate(**candidate_data)
            result = await self.db.bench_candidates.insert_one(candidate.model_dump())
            logger.info(f"Saved bench candidate: {candidate.name}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving bench candidate: {e}")
            raise
    
    async def save_open_job(self, job_data: Dict[str, Any]) -> str:
        """Save open job to database"""
        try:
            job = OpenJob(**job_data)
            result = await self.db.open_jobs.insert_one(job.model_dump())
            logger.info(f"Saved open job: {job.title}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving open job: {e}")
            raise
    
    async def save_match_result(self, match_data: Dict[str, Any]) -> str:
        """Save match result to database"""
        try:
            match = MatchResult(**match_data)
            result = await self.db.match_results.insert_one(match.model_dump())
            logger.info(f"Saved match result with score: {match.overall_score}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving match result: {e}")
            raise
    
    async def save_email_notification(self, notification_data: Dict[str, Any]) -> str:
        """Save email notification to database"""
        try:
            notification = EmailNotification(**notification_data)
            result = await self.db.email_notifications.insert_one(notification.model_dump())
            logger.info(f"Saved email notification: {notification.subject}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error saving email notification: {e}")
            raise
    
    async def get_bench_candidates(self) -> List[Dict[str, Any]]:
        """Get all bench candidates"""
        try:
            cursor = self.db.bench_candidates.find({})
            candidates = []
            async for candidate in cursor:
                candidate['_id'] = str(candidate['_id'])
                candidates.append(candidate)
            return candidates
        except Exception as e:
            logger.error(f"Error getting bench candidates: {e}")
            return []
    
    async def get_open_jobs(self) -> List[Dict[str, Any]]:
        """Get all open jobs"""
        try:
            cursor = self.db.open_jobs.find({})
            jobs = []
            async for job in cursor:
                job['_id'] = str(job['_id'])
                jobs.append(job)
            return jobs
        except Exception as e:
            logger.error(f"Error getting open jobs: {e}")
            return []
    
    async def get_job_listings(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get recent job listings"""
        try:
            cursor = self.db.job_listings.find({}).sort("created_at", -1).limit(limit)
            jobs = []
            async for job in cursor:
                job['_id'] = str(job['_id'])
                jobs.append(job)
            return jobs
        except Exception as e:
            logger.error(f"Error getting job listings: {e}")
            return []
    
    async def get_matches_by_candidate(self, candidate_id: str) -> List[Dict[str, Any]]:
        """Get matches for a specific candidate"""
        try:
            cursor = self.db.match_results.find({"candidate_id": candidate_id}).sort("overall_score", -1)
            matches = []
            async for match in cursor:
                match['_id'] = str(match['_id'])
                matches.append(match)
            return matches
        except Exception as e:
            logger.error(f"Error getting matches for candidate {candidate_id}: {e}")
            return []
    
    async def get_matches_by_job(self, job_id: str) -> List[Dict[str, Any]]:
        """Get matches for a specific job"""
        try:
            cursor = self.db.match_results.find({"job_id": job_id}).sort("overall_score", -1)
            matches = []
            async for match in cursor:
                match['_id'] = str(match['_id'])
                matches.append(match)
            return matches
        except Exception as e:
            logger.error(f"Error getting matches for job {job_id}: {e}")
            return []

    async def get_recent_matches(self, hours: int = 24):
        """Get recent matches within specified hours"""
        try:
            cutoff_time = datetime.utcnow() - timedelta(hours=hours)
            
            cursor = self.db.match_results.find({
                "created_at": {"$gte": cutoff_time},
                "notified": {"$ne": True}
            }).sort("created_at", -1)
            
            matches = []
            async for match in cursor:
                match['_id'] = str(match['_id'])
                matches.append(match)
            
            return matches
        except Exception as e:
            logger.error(f"Error getting recent matches: {e}")
            return []

    async def mark_match_notified(self, match_id: str):
        """Mark a match as notified"""
        try:
            result = await self.db.match_results.update_one(
                {"_id": ObjectId(match_id)},
                {"$set": {"notified": True, "notified_at": datetime.utcnow()}}
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error marking match as notified: {e}")
            return False

    async def get_platform_stats(self):
        """Get platform statistics"""
        try:
            stats = {}
            
            # Count documents in each collection
            stats['total_candidates'] = await self.db.candidate_profiles.count_documents({})
            stats['bench_candidates'] = await self.db.bench_candidates.count_documents({})
            stats['open_jobs'] = await self.db.open_jobs.count_documents({})
            stats['job_listings'] = await self.db.job_listings.count_documents({})
            stats['total_matches'] = await self.db.match_results.count_documents({})
            stats['recent_matches'] = await self.db.match_results.count_documents({
                "created_at": {"$gte": datetime.utcnow() - timedelta(days=7)}
            })
            stats['notified_matches'] = await self.db.match_results.count_documents({
                "notified": True
            })
            
            return stats
        except Exception as e:
            logger.error(f"Error getting platform stats: {e}")
            return {}
    
    async def update_candidate_status(self, candidate_id: str, status: str) -> bool:
        """Update candidate status"""
        try:
            result = await self.db.bench_candidates.update_one(
                {"_id": ObjectId(candidate_id)},
                {"$set": {"status": status, "updated_at": datetime.utcnow()}}
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error updating candidate status: {e}")
            return False
    
    async def update_job_status(self, job_id: str, status: str) -> bool:
        """Update job status"""
        try:
            result = await self.db.open_jobs.update_one(
                {"_id": ObjectId(job_id)},
                {"$set": {"status": status, "updated_at": datetime.utcnow()}}
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error updating job status: {e}")
            return False
    
    async def delete_old_job_listings(self, days: int = 30) -> int:
        """Delete job listings older than specified days"""
        try:
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            result = await self.db.job_listings.delete_many({
                "created_at": {"$lt": cutoff_date}
            })
            logger.info(f"Deleted {result.deleted_count} old job listings")
            return result.deleted_count
        except Exception as e:
            logger.error(f"Error deleting old job listings: {e}")
            return 0 