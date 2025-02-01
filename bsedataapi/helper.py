import requests

class Splash_downloder():

    def __init__(self):
        self.SPLASH_URL = "http://splash:8050/render.html"
        self.response = None

    def get(self,url):

        self.response = requests.get(self.SPLASH_URL, params={"url": url, "wait": 2})

    def content(self):

        return self.response.content

def get(url):
    req = Splash_downloder()
    req.get(url)

    return req.response