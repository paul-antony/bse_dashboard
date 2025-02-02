from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager



browser_options = Options()
browser_options.add_argument('--no-sandbox')
browser_options.add_argument('--headless')
browser_options.add_argument('--disable-dev-shm-usage')
browser_options.add_argument("disable-gpu")
browser_options.add_argument("--window-size=1920x1080")
browser_options.add_argument("disable-infobars")
browser_options.add_argument("--disable-extensions")
browser_options.add_argument('--disable-application-cache')



# Add custom binary paths (Render might need them)
browser_options.binary_location = "/usr/bin/firefox"

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=browser_options)
driver = webdriver.Firefox(options=browser_options)
COMMON_REQUEST_HEADERS = {
    "User-Agent": "'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'"
}