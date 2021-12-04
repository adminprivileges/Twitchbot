from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from apscheduler.schedulers.blocking import BlockingScheduler
import time, ezgmail, re, twitchbot_vars


#TODO: input python scheduler logic so that the script keeps looking for email
class Twitchbot:
    def __init__(self):
        #start the scheduler for the email search
        scheduler = BlockingScheduler()
        #run the job every 5 mins
        scheduler.add_job(self.search_emails, 'interval', minutes=5)
        scheduler.start()  
    
    
    def search_emails(self):
        #wait for emails about the EA madden stream
        self.threads = ezgmail.search('label:unread EAMaddenNFL is live!')
        if len(self.threads) > 0:
            self.open_stream()
        else:
            pass

    def get_code(self):
        #search for the email in my gmail
        self.threads = ezgmail.search('label:unread Your Twitch Login Verification Code')
        #pull the body content of the twitch verification email
        t = str(self.threads[0].messages[0].snippet)
        #i only need the 6 digit number
        self.regex_match = re.compile('\d{6}')
        self.post_match = self.regex_match.search(t)
        self.confirm_code = self.post_match.group()
        #mark as read so it wont pull up in the search again
        self.threads[0].markAsRead()
        return self.confirm_code

    def open_stream(self):
        #Setting up headless options
        options = Options()
        options.headless = True
        #This prevents me from having to dwnload the gecko self.driver
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        #im prolly gonna have to add vars later
        vars = {}
        #open straight to the stream
        self.driver.get("https://www.twitch.tv/eamaddennfl")
        print ("Headless Firefox Initialized")
        #change window size, because ive only tested at this size
        self.driver.set_window_size(1093, 960)
        #let stuff load 
        time.sleep(5)
        #scroll to the top(in case it loads you weird)
        self.driver.execute_script("window.scrollTo(0,0)")
        #click the login button
        self.driver.find_element(By.CSS_SELECTOR, ".eVigyo > .ScCoreButtonSecondary-sc-1qn4ixc-2 .Layout-sc-nxg1ff-0").click()
        self.driver.find_element(By.ID, "login-username").click()
        #send username specified in the other file
        self.driver.find_element(By.ID, "login-username").send_keys(twitchbot_vars.twitch_username)
        #send pwd
        self.driver.find_element(By.ID, "password-input").click()
        self.driver.find_element(By.ID, "password-input").send_keys(twitchbot_vars.twitch_password)
        #login
        self.driver.find_element(By.CSS_SELECTOR, ".ibRTKs").click()
        #wait a sec for the email
        time.sleep(5)
        #enter the confirmation code
        self.confirm_code = self.get_code()
        self.actions = ActionChains(self.driver)
        self.actions.send_keys(self.confirm_code[0])
        self.actions.perform()
        self.actions.send_keys(self.confirm_code[1])
        self.actions.perform()
        self.actions.send_keys(self.confirm_code[2])
        self.actions.perform()
        self.actions.send_keys(self.confirm_code[3])
        self.actions.perform()
        self.actions.send_keys(self.confirm_code[4])
        self.actions.perform()
        self.actions.send_keys(self.confirm_code[5])
        self.actions.perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(28800)
        self.driver.quit()

Twitch = Twitchbot()
Twitch()
