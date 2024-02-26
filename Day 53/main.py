import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(URL)
zillow_webpage = response.text

properties = []
property_address_list = []
property_link_list = []
property_price_list = []
soup = BeautifulSoup(zillow_webpage,'html.parser')
links = soup.find_all(name='a',href = True)
for _ in range(9,97,2):
    property_link_list.append(links[_]['href'])
address = soup.find_all(name='address')
for a in address:
    property_address_list.append(a.getText())
prices = soup.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine')
for price in prices:
    p = price.getText().strip('+/mo')
    p = p.strip('+ 1 bd')
    property_price_list.append(p)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
for _ in range(45):
    driver.get("https://forms.gle/DuHwtqZq4FYytiCVA")
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(60) # gives an implicit wait for 60 seconds

    address = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(property_address_list[_])

    price = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(property_price_list[_])

    link = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(property_link_list[_])

    submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

