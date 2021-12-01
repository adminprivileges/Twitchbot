from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, time, random

chrome_options = Options()
#chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0")
chrome_options.headless = True # also works
driver = Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)
#ser = Service(f"{os.getcwd()}/chromedriver")
#chrome_options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.get('https://www.twitch.tv/eamaddennfl')
#driver.set_window_size(1093, 960)
# 3 | runScript | window.scrollTo(0,0) |  | 
#driver.execute_script("window.scrollTo(0,0)")
# 4 | runScript | window.scrollTo(0,0) |  | 
#driver.execute_script("window.scrollTo(0,0)")
# 5 | runScript | window.scrollTo(0,0) |  | 
driver.execute_script("window.scrollTo(0,0)")
# 6 | click | css=.eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0 |  | 
#driver.implicitly_wait(10) 
#driver.find_element(By.CSS_SELECTOR, ".eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0").click()

# 7 | click | id=login-username |  | 
driver.find_element(By.ID, "login-username").click()
# 8 | type | id=login-username | thadvillain | 
driver.find_element(By.ID, "login-username").send_keys("thadvillain")
# 9 | click | id=password-input |  | 
driver.find_element(By.ID, "password-input").click()
# 10 | type | id=password-input | Tamale-Wispy5-Gently | 
driver.find_element(By.ID, "password-input").send_keys("Tamale-Wispy5-Gently")
# 11 | click | css=.ibRTKs |  | 
driver.find_element(By.CSS_SELECTOR, ".ibRTKs").click()
#play_button = driver.find_element_by_class_name("ytp-large-play-button")
#play_button.click()

time.sleep(60)
driver.quit()
