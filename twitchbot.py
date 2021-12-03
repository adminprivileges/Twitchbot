from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time, ezgmail, re, twitchbot_vars


#TODO: input python scheduler logic so that the script keeps looking for email
#TODO: Change verification to only look for unread emails

#This prevents me from having to dwnload the gecko driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#im prolly gonna have to add vars later
vars = {}
#open straight to the stream
driver.get("https://www.twitch.tv/eamaddennfl")
 #change window size, because ive only tested at this size
driver.set_window_size(1093, 960)
#let stuff load 
time.sleep(5)
#scroll to the top(in case it loads you weird)
driver.execute_script("window.scrollTo(0,0)")
#click the login button
driver.find_element(By.CSS_SELECTOR, ".eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0").click()
driver.find_element(By.ID, "login-username").click()
#send username specified in the other file
driver.find_element(By.ID, "login-username").send_keys(twitchbot_vars.twitch_username)
#send pwd
driver.find_element(By.ID, "password-input").click()
driver.find_element(By.ID, "password-input").send_keys(twitchbot_vars.twitch_password)
#login
driver.find_element(By.CSS_SELECTOR, ".ibRTKs").click()
#wait a sec for the email
time.sleep(5)
#search for the email in my gmail
threads = ezgmail.search('twitch')
#pull the body content of the twitch verification email
t = str(threads[0].messages[0].snippet)
#i only need the 6 digit number
p = re.compile('\d{6}')
s = p.search(t)
confirm_code = s.group()
#mark as read so it wont pull up in the search again
threads[0].markAsRead()
actions = ActionChains(driver)
actions.send_keys(confirm_code[0])
actions.perform()
actions.send_keys(confirm_code[1])
actions.perform()
actions.send_keys(confirm_code[2])
actions.perform()
actions.send_keys(confirm_code[3])
actions.perform()
actions.send_keys(confirm_code[4])
actions.perform()
actions.send_keys(confirm_code[5])
actions.perform()

driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,0)")
time.sleep(15)
driver.quit()