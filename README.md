<div align="center">

# 🎬 AkMovieVerse Auto Filter Bot

### A fast, configurable Telegram movie and series search bot

<a href="https://t.me/AkMovieVerse">Updates & Support</a> ·
<a href="#quick-start">Quick Start</a> ·
<a href="#commands">Commands</a>

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-See%20LICENSE-green?style=for-the-badge)

</div>

## ✨ What is AkMovieVerse?

AkMovieVerse is a feature-rich Telegram auto-filter bot for indexing files from channels, searching movies/series quickly, and delivering protected files with optional streaming and download links.

It combines a clean DreamX-based core with selected indexing, verification, premium, administration, and publishing features from the imported reference projects. The project is designed to stay configurable: enable only the features your community actually needs.

## 🚀 Feature highlights

| 🔎 Search & indexing | 🔐 Verification & access | 💎 Premium & monetization |
| --- | --- | --- |
| Automatic channel indexing | Force subscription | Premium plans |
| Fast auto-filter search | Request-to-join subscription | Referral rewards |
| MongoDB search and pagination | 1, 2, or 3 shortener stages | Redeem codes |
| Spell-check suggestions | Configurable verification delays | Telegram Stars support |
| Movie and series browsing | Group and owner-wide controls | Free-user limits |

| 🎞️ Media & publishing | 🛠️ Admin tools | 🎨 Customization |
| --- | --- | --- |
| IMDb/TMDB metadata | Broadcast and group broadcast | Custom captions |
| Streaming and download links | Ban/unban and moderation | Custom tutorials |
| Protected content | Maintenance mode | Custom IMDb templates |
| Movie/series post builder | Logs, stats, users, and chats | Custom covers and links |
| Telegraph media pages | File cleanup and deletion | Per-group settings |

Additional utilities include `/font`, `/alive`, `/ping`, `/stickerid`, and `/telegraph`.

## 🔐 Verification system

AkMovieVerse uses a simple count-based shortener flow. Select how many stages should be active:

```text
1 active shortener  → Shortener 1
2 active shorteners → Shortener 1 → Shortener 2
3 active shorteners → Shortener 1 → Shortener 2 → Shortener 3
```

Timing is measured in seconds:

```env
TWO_VERIFY_GAP=1200       # 20 minutes: first → second
THREE_VERIFY_GAP=54000    # 15 hours: second → third
```

Group admins can set the count with `/shortener_count 1`, `/shortener_count 2`, or `/shortener_count 3`.

The owner can enforce a mode and timing for every group:

```text
/global_shortener 1
/global_shortener 1,2
/global_shortener 1,2,3
/global_verify_time 1200 54000
```

Use these commands to return control to individual groups:

```text
/global_shortener reset
/global_verify_time reset
```

## 📋 Commands

### User commands

```text
/start       Start the bot
/id          Get your Telegram ID
/info        Get user or media information
/movies      Browse latest movies
/series      Browse latest series
/plan        View premium plans
/myplan      View your active premium plan
/redeem      Redeem a premium code
/font        Generate styled text
/alive       Check bot status
/ping        Check response time
/stickerid   Get a sticker ID
/telegraph   Upload replied media to Telegraph
/request     Request a file in a group
```

### Group admin commands

```text
/settings              Open group settings
/shortener_count 1     Use one shortener stage
/shortener_count 2     Use two shortener stages
/shortener_count 3     Use all three stages
/set_shortner           Configure Shortener 1
/set_shortner_2         Configure Shortener 2
/set_shortner_3         Configure Shortener 3
/set_time               Set first-to-second delay
/set_time_2             Set second-to-third delay
/set_tutorial           Set tutorial 1
/set_tutorial_2         Set tutorial 2
/set_tutorial_3         Set tutorial 3
/set_caption            Set a custom file caption
/set_template           Set an IMDb template
/set_fsub               Configure force subscription
/remove_fsub            Remove force subscription
/set_log_channel        Set verification log channel
/details                View group configuration
/verify on              Enable verification
/verify off             Disable verification
/reload                 Reload group settings
```

### Owner/admin commands

```text
/global_shortener 1       Force one stage for every group
/global_shortener 1,2     Force two stages for every group
/global_shortener 1,2,3   Force three stages for every group
/global_shortener reset   Remove the global stage override
/global_verify_time 1200 54000
/global_verify_time reset
/broadcast                Broadcast a message
/grp_broadcast             Broadcast to groups
/ban /unban /banned        Manage banned users
/stats /users /chats       View bot statistics
/maintenance               Toggle maintenance mode
/delete /deleteall         Delete indexed records
/clear_storage             Hard-delete all media indexes (admin confirmation)
/storage_details           Show MongoDB collection-wise storage usage
/deletefiles               Delete matching files
/add_premium               Add premium access
/remove_premium            Remove premium access
/premium_users             List premium users
/add_redeem                Create redeem codes
/restart                   Restart the bot
```

## ⚡ Quick start

### 1. Requirements

- Python 3.11 or newer
- MongoDB database
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- Telegram API ID and API hash from [my.telegram.org](https://my.telegram.org)
- A log channel where the bot is an administrator

### 2. Install

PowerShell:

```powershell
Set-Location "C:\path\to\autofilter-fusion-bot"
python -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Fill in the required values in `.env`, especially `BOT_TOKEN`, `API_ID`, `API_HASH`, `DATABASE_URI`, `ADMINS`, `CHANNELS`, and `LOG_CHANNEL`.

### 3. Run

```powershell
python bot.py
```

The bot registers the main user commands in Telegram automatically when it starts.

## ⚙️ Important environment variables

```env
BOT_TOKEN=your_bot_token
API_ID=your_api_id
API_HASH=your_api_hash
DATABASE_URI=mongodb_connection_string
DATABASE_NAME=Cluster0
ADMINS=123456789
CHANNELS=-1001234567890
LOG_CHANNEL=-1001234567890

IS_VERIFY=True
TWO_VERIFY_GAP=1200
THREE_VERIFY_GAP=54000
TMDB_API_KEY=optional_tmdb_api_key
TMDB_POSTER=True
```

Never commit `.env`, bot tokens, API keys, or MongoDB credentials.

## 🧭 Project layout

```text
autofilter-fusion-bot/
├── bot.py                  # Application entry point
├── info.py                 # Environment and runtime configuration
├── Script.py               # User-facing messages and templates
├── plugins/                # Telegram handlers and bot features
├── database/               # MongoDB access and indexes
├── dreamxbotz/              # Web server, streaming, and helpers
├── requirements.txt        # Python dependencies
└── .env.example            # Configuration template
```

## 🧪 Troubleshooting

**`ModuleNotFoundError`**

Install dependencies with the same Python interpreter used to launch the bot:

```powershell
python -m pip install -r requirements.txt
```

**Shortener 2 appears immediately**

Check the configured delay. Use `/details`, or set it for a group with `/set_time 1200`. For all groups, use `/global_verify_time 1200 54000`.

**TMDB errors**

Set a valid `TMDB_API_KEY`, or disable TMDB posters with `TMDB_POSTER=False`. IMDb fallback remains available.

**Bot commands are not visible**

Restart the bot after changing `bot.py`; the command menu is registered during startup.

## 🎨 Branding

Project branding: **AkMovieVerse**

Updates and support: [t.me/AkMovieVerse](https://t.me/AkMovieVerse)

Set the Telegram profile name and logo through BotFather using `/setname` and `/setuserpic`.

## 📄 License and attribution

See [LICENSE](LICENSE). This project was assembled from multiple reference projects. Preserve upstream license notices and attribution when retaining their code or assets.

<div align="center">

Made for the AkMovieVerse community · [Join the channel](https://t.me/AkMovieVerse)

</div>
