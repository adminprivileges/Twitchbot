from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
vars = {}



# Test name: twitch_signin
# Step # | name | target | value | comment
# 1 | open | /eamaddennfl |  | 
driver.get("https://www.twitch.tv/eamaddennfl")
# 2 | setWindowSize | 1093x960 |  | 
driver.set_window_size(1093, 960)
# 3 | runScript | window.scrollTo(0,0) |  | 
time.sleep(5)
driver.execute_script("window.scrollTo(0,0)")
# 6 | click | css=.eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0 |  | 
driver.find_element(By.CSS_SELECTOR, ".eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0").click()
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
time.sleep(5)
# 12 | click | css=.focus-visible |  | 
# 13 | type | css=.focus-visible | 9 | 
actions = ActionChains(driver)
actions.send_keys("9")
actions.perform()
# 14 | type | css=.focus-visible | 1 | 
actions.send_keys("1")
actions.perform()
# 15 | type | css=.focus-visible | 3 | 
actions.send_keys("3")
actions.perform()
# 16 | type | css=.focus-visible | 4 | 
actions.send_keys("4")
actions.perform()
# 17 | type | css=.focus-visible | 5 | 
actions.send_keys("5")
actions.perform()
# 18 | runScript | window.scrollTo(0,0) |  | 
driver.execute_script("window.scrollTo(0,0)")
# 19 | runScript | window.scrollTo(0,0) |  | 
driver.execute_script("window.scrollTo(0,0)")
time.sleep(15)
driver.quit()