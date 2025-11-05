# Markov Chain Text Generation Project

This project implements a **Markov Chain text generator** in Python.  
It demonstrates text generation at the **character**, **word**, and **sentence** levels using scraped data from both **static (Wikipedia)** and **dynamic (Reddit/Forum)** sources.

The focus is on **Hindi language data** and building a **basic conversational system** based on social media text patterns.

---

## 1. Project Structure

The repository contains the following core files for data acquisition and model implementation:

| File | Purpose | Data Type | Assignment Parts |
|------|----------|------------|------------------|
| `scraper.py` | Scrapes Hindi Wikipedia pages for general, article-style text and scrapes static, multi-page forums using `requests` and `BeautifulSoup` 
| `model1.ipynb` | Core logic implementing the `MarkovChain` class and running text generation tasks. 

---

## 2. Setup and Installation

This project requires **Python 3** and several external libraries, including **BeautifulSoup and Requests** for static scraping.

### Prerequisites

- **Python 3:** Ensure Python is installed.  

### Install Dependencies

Use the following command to install required libraries:

```bash
pip install requests beautifulsoup4 requests
