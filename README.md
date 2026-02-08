# Quran Player Mini App

Telegram Mini App for playing Quran recitations from itqan CMS API.

## Features

- 🎵 Play Quran recitations
- 📿 Multiple reciters and riwayahs
- ⏮️⏸️▶️⏭️ Full playback controls
- 🔀 Shuffle mode
- 🔁 Loop mode
- 📜 Playlist view
- 📱 Mobile-friendly design

## Setup

### 1. Host the App

You can host this mini app on:
- **Vercel**: Deploy the `apps/quran-player-miniapp` folder
- **Netlify**: Deploy as static site
- **GitHub Pages**: Enable in repository settings
- **Cloudflare Pages**: Deploy as static site

### 2. Configure Telegram Bot

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Create inline keyboard with mini app button
keyboard = [
    [
        InlineKeyboardButton(
            "🎵 Quran Player",
            web_app=WebAppInfo(url="https://your-domain.vercel.app/quran-player-miniapp/")
        )
    ]
]
reply_markup = InlineKeyboardMarkup(keyboard)
bot.send_message(chat_id, "Open Quran Player:", reply_markup=reply_markup)
```

### 3. Add Bot Commands

```
/quran - Open Quran Player mini app
```

## Files

```
apps/quran-player-miniapp/
├── index.html    # Mini app (16KB)
└── README.md     # This file
```

## API Integration

The mini app uses itqan CMS API:
- Base URL: https://api.cms.itqan.dev
- Recitations endpoint: /recitations/{id}/
- Audio format: R2.dev CDN URLs

## Screenshots

```
┌─────────────────────┐
│ 🎵 مشغل القرآن     │
├─────────────────────┤
│ 📿 صابر عبد الحكيم │
│ 📖 رواية عاصم     │
├─────────────────────┤
│    سورة الفاتحة    │
│    Al-Fatihah      │
├─────────────────────┤
│  🔀 ⏮️ ▶️ ⏭️ 🔁    │
├─────────────────────┤
│ ▓▓▓▓▓░░░░░░░░░░░░  │
│ 0:00 / 0:50        │
├─────────────────────┤
│ 📜 قائمة التشغيل   │
│ 1. الفاتحة ▶️      │
│ 2. البقرة         │
└─────────────────────┘
```

## Deploy to Vercel

```bash
cd apps/quran-player-miniapp
vercel --prod
```

## Bot Integration Example

```python
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler

async def quran(update: Update):
    keyboard = [[InlineKeyboardButton("🎵 Quran Player", web_app=WebAppInfo(url="YOUR_APP_URL"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("افتح مشغل القرآن:", reply_markup=reply_markup)

app = Application.builder().token("BOT_TOKEN").build()
app.add_handler(CommandHandler("quran", quran))
app.run_polling()
```
