from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(60) # gives an implicit wait for 20 seconds

# noOfArticles = driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
# noOfArticles.click()

# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

fname = driver.find_element(By.NAME,value='fName')
fname.send_keys('Harsh')

lname = driver.find_element(By.NAME,value='lName')
lname.send_keys('Gadhiya')

email = driver.find_element(By.NAME,value='email')
email.send_keys('hitpatel677@gmail.com')

submit = driver.find_element(By.CSS_SELECTOR,value='form button')
submit.click()