from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os, time, random

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0")
# chrome_options.headless = True # also works
driver = Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)
driver.get('https://www.youtube.com/watch?v=RvEqXLRocwc')
play_button = driver.find_element_by_class_name("ytp-large-play-button")
play_button.click()
time.sleep(491)

driver.quit()