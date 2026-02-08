# 🎵 Quran Player Mini App

Telegram Mini App for playing Quran recitations with multi-API support.

![Quran Player](https://img.shields.io/badge/Telegram-MiniApp-cyan?style=for-the-badge&logo=telegram)

## Features

- 🎵 Play Quran recitations from multiple sources
- 📡 Multi-API support (itqan CMS, mp3quran, everyayah, quran.com)
- 🔍 Search and filter reciters
- 👥 Multi-select reciters with checkboxes
- ⏮️⏸️▶️⏭️ Full playback controls
- 🔀 Shuffle mode
- 🔁 Loop mode
- 📜 Playlist view
- 📱 Mobile-friendly design
- 🌙 Dark theme

## Screenshots

```
┌─────────────────────────────────┐
│ 🎵 مشغل القرآن                  │
├─────────────────────────────────┤
│ ⚙️ الإعدادات                    │
│ 📡 مصادر الاستماع              │
│ ☑️ itqan CMS  ☐ mp3quran      │
│ ☑️ EveryAyah   ☐ Quran.com     │
│ 🔍 البحث عن القراء              │
│ [ابحث عن قارئ...]              │
│ ☑️ صابر عبد الحكيم             │
│ ☑️ مجد الزامل                  │
├─────────────────────────────────┤
│ 📿 صابر عبد الحكيم              │
│ 📖 رواية عاصم                  │
├─────────────────────────────────┤
│        سورة الفاتحة             │
│        Al-Fatihah              │
├─────────────────────────────────┤
│   🔀 ⏮️ ▶️ ⏭️ 🔁                │
├─────────────────────────────────┤
│ ▓▓▓░░░░░░░░░░░░░░░░░░░░░       │
│ 0:00 / 0:50                     │
├─────────────────────────────────┤
│ 📜 قائمة التشغيل (20 سورة)       │
└─────────────────────────────────┘
```

## API Sources

| Source | Status | Reciters | Riwayahs |
|--------|--------|----------|----------|
| itqan CMS | ✅ Active | 7 | 10 |
| mp3quran | ✅ Ready | 50+ | - |
| EveryAyah | ✅ Ready | 50+ | - |
| Quran.com | ✅ Ready | 30+ | ✅ |

## Quick Start

### Local Development

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/quran-player-miniapp.git
cd quran-player-miniapp

# Run local server
python3 server.py

# Open in browser
# http://localhost:8080
```

### Deploy to Netlify

1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag the `quran-player-miniapp` folder
3. Your app is live! 🎉

### Deploy to Vercel

```bash
npx vercel --prod
```

## Telegram Bot Integration

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Add to your bot
await update.message.reply_text(
    "🎵 افتح مشغل القرآن",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "▶️ تشغيل",
            web_app=WebAppInfo(url="https://YOUR_APP.netlify.app")
        )
    ]])
)
```

## File Structure

```
quran-player-miniapp/
├── index.html      # Main Mini App (24KB)
├── server.py       # Local development server
├── README.md       # This file
└── .gitignore
```

## Technologies

- HTML5, CSS3, JavaScript
- Telegram Web App SDK
- CSS Grid & Flexbox
- Dark theme gradient design

## License

MIT License - Feel free to use and modify!

---

**Made with ❤️ for the Ummah**

🌙
