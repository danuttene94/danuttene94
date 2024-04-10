#The purpose of this script is written in the README.md file.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(2)

#Go to webpage
driver.get('https://practicetestautomation.com/practice-test-login/')

#Find "username" field and type "student" into username field
username_locator = driver.find_element(By.ID, "username").send_keys("student")

#Find "password" field and type "password123" into password field
password_locator = driver.find_element(By.ID, "password").send_keys("Password123")

#Push "Submit" button and compare if actual URL is the same as "https://practicetestautomation.com/logged-in-successfully/"
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']").click()
time.sleep(2)
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

#Locate and verify that the page contains "Logged In Successfully"
logged_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = logged_locator.text
assert actual_text == "Logged In Successfully"

#Find and verify the "Log out" button is displayed on the new page
log_out_button = driver.find_element(By.LINK_TEXT, "Log out")
time.sleep(2)
assert log_out_button.is_displayed()
