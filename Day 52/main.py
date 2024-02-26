from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = 'map_of_europe'
USERNAME = '***********'
PASSWORD = '***********'

not_now = ''
'''//*[@id="mount_0_0_h/"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'''

switch_accounts = ''
'''//*[@id="mount_0_0_PW"]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div/div[2]/div[3]/span/div'''

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window() # For maximizing window
        self.driver.implicitly_wait(60) # gives an implicit wait for 60 seconds
        self.username = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username.send_keys(USERNAME)
        self.password = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        self.login = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]')
        self.login.click()
        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()
    
    
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

followerBot = InstaFollower()
followerBot.login()
followerBot.find_followers()
followerBot.follow()