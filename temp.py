from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)clear
driver.get("http://www.python.org")
assert "Python" in driver.title