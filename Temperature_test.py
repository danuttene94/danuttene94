#The purpose of this script is written in the README.md file.

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

actions = ActionChains(driver)
action = ActionChains(driver)
driver.implicitly_wait(5)


driver.get('https://10.10.10.10')
driver.find_element(By.XPATH, '//button[@class="secondary-button small-link"]').click()
time.sleep(3)
driver.find_element(By.ID, 'proceed-link').click()
time.sleep(3)
driver.get('https://10.10.10.10')
time.sleep(2)
actions.send_keys('username', Keys.TAB).perform()
time.sleep(2)
actions.send_keys('password', Keys.ENTER).perform()
time.sleep(12)
driver.find_element(By.ID, 'trigger-1023-inputEl').click()
time.sleep(2)
actions.send_keys('chassis').perform()
time.sleep(2)
driver.find_element(By.ID, 'treeview-1014-record-editChassis').click()
time.sleep(5)
driver.find_element(By.ID, 'tab-1074').click()
time.sleep(4)
pyautogui.screenshot('Temperature.png')
time.sleep(3)
