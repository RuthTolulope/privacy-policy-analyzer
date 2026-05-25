import requests
from bs4 import BeautifulSoup

def fetch_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()   #raises an exception for HTTP errors (4xx or 5xx)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator=" ", strip=True)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        if not text.strip():
            print(f"File {file_path} is empty.")
            return None
        
        return text
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except OSError as e:
        print(f"Error reading file {file_path}: {e}")
        return None