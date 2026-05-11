import requests

def fetch_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()   #raises an exception for HTTP errors (4xx or 5xx)
        return response.text
    except requests.exception.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
