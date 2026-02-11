# Quran Mini Player

Telegram Mini App for playing Quran recitations with multi-API support.

## Features

- Play Quran recitations from multiple sources
- Multi-API support (itqan CMS, EveryAyah)
- Search and filter reciters
- Full playback controls (play/pause, stop, previous, next)
- Shuffle and repeat modes
- Progress bar with seek functionality
- RTL/LTR language support
- Dark theme support
- Mobile-friendly design
- Compact player mode for small screens

## API Sources

| Source | Status | Reciters | Notes |
|--------|--------|----------|-------|
| itqan CMS | Active | 7+ | Full surah playlist with timings |
| EveryAyah | Active | 10 | Hardcoded reciter list |

## Quick Start

```bash
cd quran-player-miniapp
python3 server.py
# Open http://localhost:8080
```

## Deploy

### Netlify
Drag the folder to [Netlify Drop](https://app.netlify.com/drop)

### Vercel
```bash
npx vercel --prod
```

## File Structure

```
quran-player-miniapp/
├── index.html      # Main Mini App (~33KB)
├── server.py       # Local development server
├── README.md       # This file
└── .gitignore
```

## Technologies

- HTML5, CSS3, Vanilla JavaScript
- Telegram Web App SDK
- CSS Custom Properties for theming
- Fetch API for network requests

## License

MIT
