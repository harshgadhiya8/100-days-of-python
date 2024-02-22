from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

id = '************'
pas = '***********'
def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3813701648&f_AL=true&f_E=1&f_WT=2&keywords=data%20scientist&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(60) # gives an implicit wait for 20 seconds


signinButton = driver.find_element(By.XPATH,value="/html/body/div[1]/header/nav/div/a[2]")
signinButton.click()

email = driver.find_element(By.ID,value='username')
email.send_keys(id)

password = driver.find_element(By.ID,value='password')
password.send_keys(pas)

signin = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin.click()

apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

label = driver.find_element(by=By.CSS_SELECTOR, value="footer label")
label.click()

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
    

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

