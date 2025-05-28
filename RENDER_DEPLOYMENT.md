# AI Job Recruiter Platform - Render Deployment Guide

## Prerequisites
- ✅ Render account with GitHub authentication
- ✅ GitHub repository: `https://github.com/aideveloperindia/airecruiter.git`
- ✅ MongoDB Atlas database connection string

## Step 1: Create New Web Service on Render

1. **Login to Render Dashboard**
   - Go to [render.com](https://render.com)
   - Login with your GitHub account

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Choose "Build and deploy from a Git repository"

3. **Connect Repository**
   - Select your GitHub account
   - Choose repository: `aideveloperindia/airecruiter`
   - Click "Connect"

## Step 2: Configure Service Settings

### Basic Settings
- **Name**: `airecruiter-backend`
- **Region**: Choose closest to your users (e.g., Oregon, Frankfurt)
- **Branch**: `main`
- **Root Directory**: Leave empty (uses repository root)
- **Runtime**: `Python 3`

### Build & Deploy Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python src/main.py`

### Advanced Settings
- **Auto-Deploy**: ✅ Enabled (deploys automatically on git push)

## Step 3: Environment Variables

Add the following environment variables in Render dashboard:

### Required Variables
```
MONGODB_URI=mongodb+srv://aideveloperindia:1Aditya%401Pranitha%40100@airecruiter.0l8ted7.mongodb.net/?retryWrites=true&w=majority&appName=airecruiter
ENVIRONMENT=production
PORT=10000
```

### Optional Variables (for email functionality)
```
GMAIL_EMAIL=your-gmail@gmail.com
GMAIL_PASSWORD=your-app-password
```

### How to Add Environment Variables:
1. In your service dashboard, go to "Environment" tab
2. Click "Add Environment Variable"
3. Add each variable with key-value pairs
4. Click "Save Changes"

## Step 4: Deploy

1. **Start Deployment**
   - Click "Create Web Service"
   - Render will automatically start building and deploying

2. **Monitor Build Process**
   - Watch the build logs in real-time
   - Build typically takes 3-5 minutes

3. **Verify Deployment**
   - Once deployed, you'll get a URL like: `https://airecruiter-backend.onrender.com`
   - Test the health endpoint: `https://your-app.onrender.com/health`

## Step 5: Test API Endpoints

### Health Check
```bash
curl https://your-app.onrender.com/health
```

### Scrape Jobs
```bash
curl -X POST "https://your-app.onrender.com/scrape-jobs?query=python developer&location=India&max_jobs=5"
```

### Get Platform Stats
```bash
curl https://your-app.onrender.com/stats
```

### Run Full Cycle
```bash
curl -X POST "https://your-app.onrender.com/run-full-cycle?query=software engineer&location=India&max_jobs=10"
```

## Step 6: API Documentation

Once deployed, access interactive API documentation at:
- **Swagger UI**: `https://your-app.onrender.com/docs`
- **ReDoc**: `https://your-app.onrender.com/redoc`

## Available API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Basic health check |
| GET | `/health` | Detailed health check |
| POST | `/scrape-jobs` | Scrape jobs from Indeed |
| POST | `/find-matches` | Find candidate-job matches |
| POST | `/send-notifications` | Send email notifications |
| POST | `/run-full-cycle` | Complete job matching cycle |
| GET | `/stats` | Platform statistics |

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check requirements.txt for correct package versions
   - Verify Python version compatibility

2. **Database Connection Issues**
   - Verify MONGODB_URI is correctly URL-encoded
   - Check MongoDB Atlas network access settings

3. **Service Won't Start**
   - Check start command: `python src/main.py`
   - Verify PORT environment variable is set to 10000

4. **Import Errors**
   - Ensure all dependencies are in requirements.txt
   - Check file paths and module imports

### Logs and Monitoring

1. **View Logs**
   - Go to your service dashboard
   - Click "Logs" tab to see real-time logs

2. **Monitor Performance**
   - Check "Metrics" tab for CPU/Memory usage
   - Monitor response times and error rates

## Free Tier Limitations

Render Free Tier includes:
- ✅ 750 hours/month (enough for continuous running)
- ✅ Automatic SSL certificates
- ✅ Custom domains
- ⚠️ Services sleep after 15 minutes of inactivity
- ⚠️ Cold start delay when waking up

## Production Considerations

For production use, consider upgrading to paid plan for:
- No sleep/cold starts
- More CPU and memory
- Priority support
- Advanced monitoring

## Security Best Practices

1. **Environment Variables**
   - Never commit sensitive data to git
   - Use Render's environment variable system

2. **Database Security**
   - Use MongoDB Atlas IP whitelist
   - Rotate database passwords regularly

3. **API Security**
   - Consider adding API key authentication
   - Implement rate limiting for production

## Next Steps

1. **Test all endpoints** to ensure functionality
2. **Set up monitoring** for production use
3. **Configure email service** for notifications
4. **Add sample data** to test matching system
5. **Integrate with frontend** application

## Support

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **MongoDB Atlas**: [docs.atlas.mongodb.com](https://docs.atlas.mongodb.com)
- **FastAPI Documentation**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)

---

**Deployment URL**: Your app will be available at `https://airecruiter-backend.onrender.com`

**Status**: Ready for deployment! 🚀 