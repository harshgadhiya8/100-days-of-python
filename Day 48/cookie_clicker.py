from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

tt_end = time.time() + 300
while time.time() < tt_end: #5 minute outer loop
    t_end = time.time() + 5
    while time.time() < t_end: #5 second inner loop
        cookie.click()
    store_items = driver.find_elements(By.CSS_SELECTOR,value = '#store div') 
    for n in range(len(store_items) - 1, 0, -1): #iterate from most expensive items
        try:
            store_items[n].get_attribute('onclick') #test for click
            store_items[n].click()
        except:
            pass
 
cps = driver.find_element(By.CSS_SELECTOR,value='#cps')
print(cps.text)
 
driver.close()
