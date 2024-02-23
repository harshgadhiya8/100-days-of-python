from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(60) # gives an implicit wait for 20 seconds

login = driver.find_element(By.XPATH, value='//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

#//*[@id="c-1177047094"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button

fb_login = driver.find_element(By.XPATH, value='//*[@id="c-1177047094"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.NAME,value='email')
email.send_keys('*********')
pas = driver.find_element(By.NAME,value='pass')
pas.send_keys('********')

submit = driver.find_element(By.NAME,value='login')
submit.click()

sleep(5)
location = driver.find_element(By.XPATH,value='//*[@id="c-1177047094"]/main/div/div/div/div[3]/button[1]')
location.click()

notification = driver.find_element(By.XPATH,value='//*[@id="c-1177047094"]/main/div/div/div/div[3]/button[2]')
notification.click()

cookies = driver.find_element(By.XPATH,value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

try:
    print("called")
    like_button = driver.find_element(By.XPATH,value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
except ElementClickInterceptedException:
    try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    except NoSuchElementException:
            sleep(2)

            