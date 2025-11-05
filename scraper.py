import requests 
import os 
import re
from bs4 import BeautifulSoup
import time

def scrape_url(url):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:

            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            paras = soup.find_all('p')
            raw_text = "\n".join([p.get_text() for p in paras])
            cleaned_text = re.sub(r'\[.*?\]', '', raw_text)
            return cleaned_text
        except Exception as e:
            print(e)

def scrape_all(urls_list, output_file):
    try:
        with open(output_file, 'a', encoding='utf-8') as f:
            for i, url in enumerate(urls_list):
                cleaned_text = scrape_url(url)
                if cleaned_text:
                    f.write(cleaned_text)
                
                if i < len(urls_list) - 1:
                    time.sleep(2)
        print("Scraping complete lol")
    except Exception as e:
        print(e)
        


if __name__ == "__main__":
    
    
    urls_list = [
    "https://hi.wikipedia.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%AA%E0%A4%BE%E0%A4%A8",
    "https://hi.wikipedia.org/wiki/%E0%A4%B0%E0%A5%82%E0%A4%B8",
    "https://hi.wikipedia.org/wiki/%E0%A4%B8%E0%A4%82%E0%A4%AF%E0%A5%81%E0%A4%95%E0%A5%8D%E0%A4%A4_%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A5%8D%E0%A4%AF_%E0%A4%85%E0%A4%AE%E0%A5%87%E0%A4%B0%E0%A4%BF%E0%A4%95%E0%A4%BE"
    ]

    output_file = "output_language_text.txt"

    if os.path.exists(output_file):
        os.remove(output_file)
    
    scrape_all(urls_list=urls_list, output_file=output_file)

    

    
    

    
        

