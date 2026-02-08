# Push to GitHub

## 1. Create Repository on GitHub

Go to: https://github.com/new

- **Repository name**: `quran-player-miniapp`
- **Description**: "Telegram Mini App for Quran Player with multi-API support"
- **Public**: ✅ Yes
- **No** .gitignore, No README (we have them)

## 2. Push Commands

```bash
cd ~/.openclaw/workspace/apps/quran-player-miniapp

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/quran-player-miniapp.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## 3. Deploy to Netlify

1. Go to: https://app.netlify.com/sites/new
2. Click **"Add new site"** → **"Import an existing project"**
3. Select **GitHub** and choose `quran-player-miniapp`
4. Settings (leave defaults):
   - Build command: (empty)
   - Publish directory: (empty)
5. Click **"Deploy site"**

## 4. Get Your URL

After deployment, Netlify will give you:
```
https://quran-player-miniapp-xxxxx.netlify.app
```

## 5. Use with Telegram Bot

```python
WEB_APP_URL = "https://quran-player-miniapp-xxxxx.netlify.app"

keyboard = [[InlineKeyboardButton(
    "🎵 Quran Player",
    web_app=WebAppInfo(url=WEB_APP_URL)
)]]
```

---

**Done!** 🎉
