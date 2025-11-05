# Markov Chain Text Generation Project

This project implements a **Markov Chain text generator** in Python.  
It demonstrates text generation at the **character**, **word**, and **sentence** levels using scraped data from both **static (Wikipedia)** and **dynamic (Reddit/Forum)** sources.

The focus is on **Hindi language data** and building a **basic conversational system** based on social media text patterns.

---

## 1. Project Structure

The repository contains the following core files for data acquisition and model implementation:

| File | Purpose | Data Type | Assignment Parts |
|------|----------|------------|------------------|
| `scraper.py` | Scrapes Hindi Wikipedia pages for general, article-style text. | Article | Parts A & C |
| `scraper_reddit.py` | (Recommended) Scrapes multiple subreddits dynamically using Selenium for conversational posts/titles. | Conversational | Part D |
| `forum_scraper.py` | (Alternative) Scrapes static, multi-page forums using `requests` and `BeautifulSoup`. | Conversational | Part D (Alternative) |
| `markov_generator.py` | Core logic implementing the `MarkovChain` class and running text generation tasks. | Both | Parts A, C & D |

---

## 2. Setup and Installation

This project requires **Python 3** and several external libraries, including **Selenium** for dynamic scraping.

### Prerequisites

- **Python 3:** Ensure Python is installed.  
- **Chrome/Chromium Browser:** Required for `scraper_reddit.py`.  
- **ChromeDriver:** Download the correct version of ChromeDriver that matches your Chrome/Chromium browser and add it to your system `PATH`.

### Install Dependencies

Use the following command to install required libraries:

```bash
pip install requests beautifulsoup4 selenium
