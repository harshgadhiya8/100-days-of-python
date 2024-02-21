from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(60) # gives an implicit wait for 20 seconds

# price_dollar = driver.find_element(by='class name',value="a-price-whole")
# price_cents = driver.find_element(by='class name',value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text} dollars")

# search_bar = driver.find_element(by='name',value='q')
# button = driver.find_element(by='id',value='submit')
# print(search_bar.get_attribute('placeholder'))
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR,value='.documentation-widget a')
# print(link.text)

# doc_url = driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(doc_url.text)

event_times = driver.find_elements(By.CSS_SELECTOR,value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR,value='.event-widget li a')
events = {}
for n in range(len(event_times)):
    events[n] ={
        'time':event_times[n].text,
        'name':event_names[n].text
    }
print(events)
driver.quit()
