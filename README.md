# Facebook Scraper for Python

<div align="center">

<img src="https://img.shields.io/badge/Thordata-Official-blue?style=for-the-badge" alt="Thordata Logo">

**Extract posts, events, profiles, and comments from Facebook at scale.**  
*Powered by Thordata's residential proxy network & Web Scraper API.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Powered By](https://img.shields.io/badge/Powered%20By-Thordata-orange)](https://dashboard.thordata.com/?utm_source=github&utm_medium=readme&utm_campaign=facebook_scraper)

</div>

---

## ⚡ Features

- **📝 Posts**: Scrape Facebook post details by posts URL.
- **📅 Events**: Get events by event list URL, search URL, or events URL.
- **👤 Profiles**: Extract Facebook profile information.
- **💬 Comments**: Get post comments with sorting options (Most Relevant, Newest, All comments).
- **Managed Requests:** Uses Thordata's Web Scraper API for request handling and proxy management.
- **Batch Support**: Most crawlers support batch mode, allowing multiple tasks to be submitted at once.

## 🚀 Quick Start

### 1. Get Credentials

Get your **free** scraping token from the [Thordata Dashboard](https://dashboard.thordata.com/?utm_source=github&utm_medium=readme&utm_campaign=facebook_scraper).

### 2. Install

```bash
git clone https://github.com/Thordata/facebook-scraper-python.git
cd facebook-scraper-python
pip install -r requirements.txt
```

### 3. Configure

Copy `.env.example` to `.env` and fill in your tokens:

```ini
THORDATA_SCRAPER_TOKEN=your_token
THORDATA_PUBLIC_TOKEN=your_public
THORDATA_PUBLIC_KEY=your_key
```

### 4. Run Examples

#### 1. Facebook Posts Scraper

```bash
python main.py post "https://www.facebook.com/permalink.php?story_fbid=pfbid0gNjZBhqCxSqj9xJS5aygNwqFqNEM2fYbTFKKbsvvGdEfTgFyAYWSckvkEHPqAE7gl%26id=61574926580533%26rdid=86oaujwNGCCdPLfj#"
```

#### 2. Facebook Events Scraper

**By Event List URL:**
```bash
python main.py event eventlist "https://www.facebook.com/nohoclub/events" --upcoming-events-only "true"
```

**By Search URL (multiple URLs supported):**
```bash
python main.py event search "https://www.facebook.com/events/explore/us-atlanta/107991659233606" "https://www.facebook.com/events/search/?q=Linkin%20Park"
```

**By Events URL (multiple URLs supported):**
```bash
python main.py event events "https://www.facebook.com/events/1546764716269782" "https://www.facebook.com/events/807311478247339/807311481580672"
```

#### 3. Facebook Profile Scraper

```bash
python main.py profile "https://www.facebook.com/MayeMusk"
```

#### 4. Facebook Post Comments Scraper

```bash
python main.py comment "https://www.facebook.com/share/p/1K6xfHFkrK/" --get-all-replies "True" --limit-records "5" --comments-sort "All comments"
```

**Comments Sort Options:**
- `Most Relevent`
- `Newest`
- `All comments`

All data is saved to `output/` in JSON format.

---

## 🏗️ How it Works

This scraper uses **Thordata's Web Scraper API (Hybrid Mode)**:
1.  **Task Creation**: Sends scraping parameters to Thordata's cloud cluster.
2.  **Auto-Polling**: The SDK (`run_task`) automatically polls for completion.
3.  **Result Retrieval**: Downloads the clean JSON data once ready.

This architecture ensures you **never get blocked** and receive clean, structured data.

---

## What This Example Does Not Collect

This repository is an example client for authorized Thordata Web Scraper API requests. It does not include Facebook login cookies, private account access, or browser session data.

The example does not grant rights to collect, reuse, train on, or redistribute third-party Facebook content. Use it only for lawful and authorized workflows.

Never place API keys, cookies, personal information, or private data in source files, logs, README files, or commits.

## Failure Behavior

Requests may fail because of invalid credentials, unsupported parameters, rate limits, endpoint restrictions, or temporary service errors.

When a request fails, treat the response as an error rather than valid Facebook data. Check the terminal output and returned API response for details. Exact error codes and limits depend on the account and endpoint.

## For Coding Assistants

When modifying or running this example:

- Read `.env.example` and keep credentials in environment variables.
- Check the existing configuration before inventing scraper IDs or request parameters.
- Preserve the current Web Scraper API request flow.
- Never print or commit API keys, cookies, private URLs, or personal data.
- Review returned post, event, profile, and comment data before sharing it.
- Treat returned Facebook data as third-party data subject to applicable terms and usage restrictions.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
