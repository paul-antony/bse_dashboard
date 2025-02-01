import requests
from bs4 import BeautifulSoup
from pprint import pprint


import requests

class Splash_downloder():

    def __init__(self):
        self.SPLASH_URL = "http://localhost:8050/render.html"
        self.response = None

    def get(self,url):

        self.response = requests.get(self.SPLASH_URL, params={"url": url, "wait": 2})

    def page_source(self):
        return self.response.text

        



# Test URL (replace with any webpage)
TEST_URL = "https://www.python.org/"

def scrape_page(url):

    driver = Splash_downloder()
    driver.get(TEST_URL)
    response = driver.response
    pprint(vars(response))



    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source(), "html.parser")

    # Extract data (modify as needed)
    title = soup.title.text if soup.title else "No title found"

    return {"url": url, "title": title}

if __name__ == "__main__":
    result = scrape_page(TEST_URL)
    #print(result)