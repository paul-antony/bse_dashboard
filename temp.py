import requests
from bs4 import BeautifulSoup

# Splash server URL (make sure Splash is running)
SPLASH_URL = "http://localhost:8050/render.html"

# Test URL (replace with any webpage)
TEST_URL = "https://www.python.org/"

def scrape_page(url):
    """Fetch page using Splash and extract data"""
    response = requests.get(SPLASH_URL, params={"url": url, "wait": 2})

    if response.status_code != 200:
        print(f"Error: Failed to fetch {url}, Status Code:", response.status_code)
        return None

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract data (modify as needed)
    title = soup.title.text if soup.title else "No title found"

    return {"url": url, "title": title}

if __name__ == "__main__":
    result = scrape_page(TEST_URL)
    print(result)