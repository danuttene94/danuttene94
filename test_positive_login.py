#The purpose of this script is written in the README.md file
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import pyscreeze
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

actions = ActionChains(driver)
action = ActionChains(driver)
driver.implicitly_wait(5)


driver.get('https://10.10.10.10')
driver.find_element(By.XPATH, '//button[@class="secondary-button small-link"]').click()
driver.find_element(By.ID, 'proceed-link').click()
driver.get('https://10.10.10.10')
actions.send_keys('username', Keys.TAB).perform()
actions.send_keys('password', Keys.ENTER).perform()
time.sleep(13)
driver.find_element(By.ID, 'saveConfigButton').click()
time.sleep(3)
driver.find_element(By.ID, 'button-1006').click()
driver.find_element(By.ID, 'refreshButton-btnEl').click()
driver.find_element(By.ID, 'Port_193').click()
driver.find_element(By.ID, 'editButton').click()
driver.find_element(By.ID, 'graphButton-btnIconEl').click()
driver.find_element(By.ID, 'helpButton-btnIconEl').click()
original_window = driver.current_window_handle
driver.switch_to.window(original_window)
time.sleep(3)
driver.find_element(By.ID, 'helpDocumentationButton').click()
driver.switch_to.window(original_window)
time.sleep(3)
driver.find_element(By.ID, 'trigger-1023-inputEl').click()
actions.send_keys('chassis').perform()
time.sleep(5)
driver.find_element(By.ID, 'treeview-1014-record-editChassis').click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite('image version')
pyautogui.hotkey('Return')
pyautogui.screenshot('image_version.png')
