# 🚀 Deployment Guide

## GitHub Setup ✅ COMPLETED

Your repository is now connected to GitHub at:
**https://github.com/aideveloperindia/airecruiter.git**

### What's Included:
- ✅ Complete AI Job Platform (Python Backend)
- ✅ Next.js Frontend with AI Resume Analysis
- ✅ MongoDB Atlas Integration
- ✅ Comprehensive Documentation
- ✅ Professional README with badges

## 🌐 Vercel Deployment (Frontend)

### Step 1: Connect to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign in with your GitHub account: **aideveloperindia@gmail.com**
3. Click "New Project"
4. Import your repository: `aideveloperindia/airecruiter`

### Step 2: Configure Deployment
```
Framework Preset: Next.js
Root Directory: temp-project
Build Command: npm run build
Output Directory: .next
Install Command: npm install
```

### Step 3: Environment Variables (Optional)
No environment variables needed for frontend.

### Step 4: Deploy
- Vercel will auto-deploy from the `temp-project` directory
- Your app will be available at: `https://airecruiter-[random].vercel.app`

## 🐍 Backend Deployment Options

### Option 1: Railway (Recommended)
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Select `ai-job-platform` directory
4. Add environment variables:
   ```
   MONGODB_URI=mongodb+srv://aideveloperindia:1Aditya%401Pranitha%40100@airecruiter.0l8ted7.mongodb.net/?retryWrites=true&w=majority&appName=airecruiter
   EMAIL_USER=aideveloperindia@gmail.com
   EMAIL_PASSWORD=[your-gmail-app-password]
   EMAIL_FROM=aideveloperindia@gmail.com
   ```

### Option 2: Heroku
```bash
cd ai-job-platform
heroku create ai-job-platform-[your-name]
heroku config:set MONGODB_URI="your-mongodb-uri"
git push heroku main
```

### Option 3: DigitalOcean App Platform
1. Connect GitHub repository
2. Select `ai-job-platform` directory
3. Choose Python runtime
4. Add environment variables

## 🔧 Post-Deployment

### Frontend URL
Your Next.js app will be available at:
`https://airecruiter-[random].vercel.app`

### Backend URL
Your Python API will be available at:
`https://your-backend-url.com`

### Update Frontend API Calls
If you deploy the backend, update the API endpoints in your Next.js app to point to your deployed backend URL.

## 📧 Gmail App Password Setup

For email notifications to work:
1. Go to Google Account settings
2. Enable 2-Factor Authentication
3. Generate App Password for "Mail"
4. Use this password in `EMAIL_PASSWORD` environment variable

## 🎯 Next Steps

1. **Deploy Frontend to Vercel** (5 minutes)
2. **Deploy Backend to Railway** (10 minutes)
3. **Set up Gmail App Password** (5 minutes)
4. **Test the complete system** (5 minutes)

Total deployment time: ~25 minutes

## 🆘 Troubleshooting

### Common Issues:
- **Build fails**: Check Node.js version (use 18+)
- **MongoDB connection**: Verify connection string encoding
- **Email not working**: Check Gmail App Password setup
- **CORS errors**: Add your Vercel domain to backend CORS settings

## 📞 Support

For deployment help:
- Email: aideveloperindia@gmail.com
- GitHub Issues: https://github.com/aideveloperindia/airecruiter/issues 