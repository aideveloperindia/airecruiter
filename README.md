# 🤖 AI Recruiter - Complete Platform

[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green)](https://mongodb.com)
[![Next.js](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![AI](https://img.shields.io/badge/AI-TF--IDF-orange)](https://scikit-learn.org)

A comprehensive AI-powered recruitment platform that combines intelligent job matching with modern web technologies. Features automated job scraping, AI-based candidate matching, and a beautiful Next.js frontend.

## 🌟 Features

### 🔍 **AI Job Matching Platform (Backend)**
- **Multi-Portal Scraping**: Indeed, Naukri, Foundit.in, Wellfound, LinkedIn Jobs
- **AI-Powered Matching**: TF-IDF + Cosine Similarity with multi-factor scoring
- **MongoDB Atlas Integration**: Scalable cloud database with optimized indexes
- **Automated Scheduling**: APScheduler for 6-12 hour matching cycles
- **Email Notifications**: Gmail SMTP integration for match alerts
- **Ethical Scraping**: Rate limiting, user agent rotation, robots.txt compliance

### 💻 **Modern Frontend (Next.js)**
- **AI Resume Analysis**: Real PDF text extraction and parsing
- **Glassmorphism UI**: Modern, beautiful interface design
- **Real-time Dashboard**: Live candidate and job data
- **Responsive Design**: Mobile-first approach
- **Demo Integration**: Sundar Pichai demo with realistic data

## 🏗️ Project Structure

```
airecruiter/
├── 🐍 ai-job-platform/          # Python Backend
│   ├── config/                  # Environment configuration
│   ├── database/                # MongoDB models & connections
│   ├── scrapers/                # Job portal scrapers
│   ├── ai_matching/             # AI matching algorithms
│   ├── src/                     # Core application logic
│   ├── tests/                   # Test files
│   └── requirements.txt         # Python dependencies
│
├── ⚛️ temp-project/             # Next.js Frontend
│   ├── src/                     # React components & pages
│   ├── public/                  # Static assets
│   └── package.json             # Node.js dependencies
│
└── 📦 version1/                 # Backup of original version
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+
- MongoDB Atlas account
- Gmail account (for notifications)

### Backend Setup
```bash
cd ai-job-platform
pip install -r requirements.txt

# Configure environment
cp env_example.txt .env
# Edit .env with your MongoDB and Gmail credentials

# Test the system
python simple_test.py

# Run full demo
python test_demo.py
```

### Frontend Setup
```bash
cd temp-project
npm install
npm run dev
```

Visit `http://localhost:3001` to see the application.

## ⚙️ Configuration

### MongoDB Atlas
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_DATABASE=ai_job_platform
```

### Gmail SMTP
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com
```

## 🤖 AI Matching Algorithm

The platform uses a sophisticated multi-factor matching system:

1. **Text Similarity**: TF-IDF vectorization + cosine similarity
2. **Skills Overlap**: Jaccard similarity for skill matching
3. **Location Matching**: Geographic proximity scoring
4. **Experience Alignment**: Years of experience comparison
5. **Composite Scoring**: Weighted combination of all factors

## 📊 Database Schema

### Collections
- `job_listings`: Scraped job postings
- `candidate_profiles`: Candidate information
- `bench_candidates`: Internal bench candidates
- `open_jobs`: Company job openings
- `matches`: AI-generated matches
- `email_notifications`: Email tracking

## 🌐 Deployment

### Backend Deployment
- **Heroku**: `git push heroku main`
- **Railway**: Connect GitHub repository
- **DigitalOcean**: Docker deployment ready

### Frontend Deployment (Vercel)
1. Connect GitHub repository to Vercel
2. Vercel auto-detects Next.js configuration
3. Deploy with zero configuration

### Environment Variables
Set these in your deployment platform:
- `MONGODB_URI`
- `EMAIL_USER`
- `EMAIL_PASSWORD`
- `EMAIL_FROM`

## 🔧 API Endpoints

```
POST /api/scrape          # Trigger job scraping
GET  /api/jobs            # Get job listings
GET  /api/candidates      # Get candidates
POST /api/match           # Run AI matching
GET  /api/matches         # Get match results
```

## 📈 Performance

- **Matching Speed**: ~1000 candidates/minute
- **Scraping Rate**: 50-100 jobs/minute (with ethical delays)
- **Database**: Optimized indexes for sub-second queries
- **Scalability**: Horizontal scaling ready

## 🛡️ Security

- **Environment Variables**: Sensitive data protection
- **Rate Limiting**: Prevents abuse
- **Input Validation**: Pydantic models
- **CORS Protection**: Secure API access

## 🧪 Testing

```bash
# Backend tests
cd ai-job-platform
python -m pytest tests/

# Frontend tests
cd temp-project
npm test
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**AI Developer India**  
📧 Email: aideveloperindia@gmail.com  
🐙 GitHub: [@aideveloperindia](https://github.com/aideveloperindia)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📞 Support

For support, email aideveloperindia@gmail.com or create an issue on GitHub.

---

⭐ **Star this repository if you found it helpful!** 