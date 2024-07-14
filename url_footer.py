import requests
from bs4 import BeautifulSoup
import re
import csv
from urllib.request import Request, urlopen

def fetch_footer_year(url):
    try:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
}
        #req = Request(url,headers=headers)
        #page = urlopen(req)
        #soup = BeautifulSoup(page,'html.parser')
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        footer = soup.find('footer')
        if footer:
            year_match = re.search(r'\b(19|20)\d{2}\b', footer.text)
            if year_match:
                return year_match.group()
            else:
                return "Year not found"
        else:
            return "No footer found"
    except Exception as e:
        return f"Error: {e}"

def process_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    results = [("URL", "Footer Year")]
    for url in urls:
        year = fetch_footer_year(url)
        results.append((url, year))
        print(f"Processed {url}")

    with open('footer_years.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(results)
        print("Results saved to footer_years.csv")

# Replace 'urls.txt' with the path to your file containing URLs
process_urls('urls.txt')