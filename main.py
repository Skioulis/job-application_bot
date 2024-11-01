import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4057647525&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
load_dotenv(dotenv_path=".env")
linkedin_username = os.getenv("mail")
linkedin_password = os.getenv("password")

def driver_initialization (url : str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    inner_driver = webdriver.Chrome(options=chrome_options)
    inner_driver.get(url)
    return inner_driver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)

driver = driver_initialization(URL)

sleep(3)

sign_in_button = driver.find_element(By.CLASS_NAME, value="sign-in-modal__outlet-btn")

sign_in_button.click()

sleep(3)

username_input = driver.find_element(By.ID , value="base-sign-in-modal_session_key")
password_input = driver.find_element(By.ID , value="base-sign-in-modal_session_password")
second_sign_in_button = driver.find_element(By.CLASS_NAME, value='sign-in-form__submit-btn--full-width')

username_input.send_keys(linkedin_username)
password_input.send_keys(linkedin_password)
second_sign_in_button.click()

sleep(5)

# driver.quit()
