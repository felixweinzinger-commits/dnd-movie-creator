# Deploy to Streamlit Cloud - 25 Minutes

## What is Streamlit Cloud?

Free hosting for Streamlit apps. Your app runs online 24/7.

✅ Free forever  
✅ No setup  
✅ Auto-updates from GitHub  
✅ Anyone can access via URL  

---

## Step 1: Create GitHub Account (5 min)

1. Go to: https://github.com
2. Click "Sign up"
3. Enter email, password, username
4. Verify email
5. Done!

---

## Step 2: Create GitHub Repository (5 min)

1. Go to: https://github.com/new
2. **Repository name:** `dnd-movie-generator`
3. **Public** (important for Streamlit Cloud)
4. Check "Add a README file"
5. Click "Create repository"

---

## Step 3: Push Code to GitHub (5 min)

### Option A: Using Git Commands

```bash
cd C:\Users\admin\Projects\dnd-movie-generator
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/dnd-movie-generator.git
git branch -M main
git push -u origin main
```

### Option B: Using GitHub Desktop (Easier)

1. Download: https://desktop.github.com/
2. Sign in with GitHub
3. Click "Add" → "Add Existing Repository"
4. Select your project folder
5. Click "Publish to GitHub"

---

## Step 4: Sign Up for Streamlit Cloud (5 min)

1. Go to: https://streamlit.io/cloud
2. Click "Sign up"
3. Choose "Sign up with GitHub"
4. Authorize Streamlit
5. Done!

---

## Step 5: Deploy Your App (5 min)

On Streamlit Cloud dashboard:

1. Click "New app"
2. Select your repository: `dnd-movie-generator`
3. Branch: `main`
4. Main file path: `streamlit_app.py`
5. Click "Deploy!"

Streamlit will automatically:
- ✅ Install dependencies
- ✅ Run your app
- ✅ Give you a live URL

---

## Your Live URL

After deployment, you get:
```
https://YOUR-USERNAME-dnd-movie-generator-xxxxx.streamlit.app
```

Share this URL with anyone!

---

## Adding API Keys (Optional)

Don't commit keys to GitHub! Instead:

1. Go to: https://share.streamlit.io/
2. Select your app
3. Go to "Advanced settings"
4. Click "Secrets"
5. Add:
   ```
   OPENAI_API_KEY = "sk-..."
   PIKA_API_KEY = "..."
   ELEVENLABS_API_KEY = "..."
   ```

---

## Auto-Updates

After first deployment:
- Make code changes locally
- Push to GitHub: `git push`
- Streamlit auto-redeploys!

No manual deployment needed.

---

## Limitations

Free tier has:
- ✅ 1 app
- ✅ 24/7 uptime
- ✅ Unlimited traffic
- ⚠️ 1 GB memory
- ⚠️ Resets after 7 days inactivity

This is fine for most uses!

---

## Quick Checklist

- [ ] GitHub account created
- [ ] GitHub repo created  
- [ ] Code pushed to GitHub
- [ ] Streamlit account created
- [ ] App deployed
- [ ] Live URL working
- [ ] Shared with others!

---

## Total Time: ~25 minutes

Then your app is **live online forever!** 🚀

---

## Next: Do This Now

1. Create GitHub account: https://github.com
2. Follow steps above
3. Share your live URL!

Questions? See full guide or Streamlit docs.

---

**Your D&D Movie Generator is about to be live!** 🎬🐉
