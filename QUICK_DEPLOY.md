# 🚀 Quick Deploy to Render - 5 Minutes Setup

## ✅ Prerequisites Complete
- [x] Render account with GitHub authentication
- [x] GitHub repository pushed with latest changes
- [x] MongoDB Atlas connection string ready

## 🎯 Deploy Now - Follow These Steps:

### 1. Go to Render Dashboard
👉 **[Open Render Dashboard](https://dashboard.render.com)**

### 2. Create New Web Service
- Click **"New +"** → **"Web Service"**
- Select **"Build and deploy from a Git repository"**
- Connect **GitHub** → Choose **`aideveloperindia/airecruiter`**

### 3. Configure Service (Copy-Paste Ready)

**Service Name:**
```
airecruiter-backend
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
python src/main.py
```

**Environment Variables** (Add these in Environment tab):
```
MONGODB_URI=mongodb+srv://aideveloperindia:1Aditya%401Pranitha%40100@airecruiter.0l8ted7.mongodb.net/?retryWrites=true&w=majority&appName=airecruiter
ENVIRONMENT=production
PORT=10000
```

### 4. Deploy
- Click **"Create Web Service"**
- Wait 3-5 minutes for build completion
- Your API will be live at: `https://airecruiter-backend-XXXX.onrender.com`

### 5. Test Deployment
Once deployed, test these URLs in your browser:

**Health Check:**
```
https://your-app-url.onrender.com/health
```

**API Documentation:**
```
https://your-app-url.onrender.com/docs
```

## 🎉 That's It!

Your AI Job Recruiter Platform backend is now live and ready to:
- ✅ Scrape jobs from Indeed
- ✅ Match candidates with AI
- ✅ Send email notifications
- ✅ Provide REST API for frontend integration

## 📱 Next Steps After Deployment:

1. **Test API endpoints** using the interactive docs
2. **Add sample candidates** to test matching
3. **Configure Gmail** for email notifications (optional)
4. **Integrate with your frontend** application

## 🆘 Need Help?

- **Build failing?** Check the logs in Render dashboard
- **Database issues?** Verify MongoDB URI is correct
- **Questions?** Refer to `RENDER_DEPLOYMENT.md` for detailed guide

---

**⏱️ Total Time: ~5 minutes**
**💰 Cost: FREE (Render free tier)**
**🔄 Auto-deploy: Enabled (updates on git push)** 