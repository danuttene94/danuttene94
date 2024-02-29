from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyscreeze
import time

cService = webdriver.ChromeService(
    executable_path=r'C:\Users\USER\PycharmProjects\pythonProject\chromedriver.exe')

driver = webdriver.Chrome(service=cService)
print(driver.service.is_connectable())  # print True
driver.maximize_window()

actions = ActionChains(driver)
action = ActionChains(driver)
driver.implicitly_wait(15)


def test_edm_login():
    #This step opens the switch IP
    driver.get('https://10.10.10.10')
    
    #These two steps below help passing over the security warning
    driver.find_element(By.XPATH, '//button[@class="secondary-button small-link"]').click()
    driver.find_element(By.ID, 'proceed-link').click()
    
    #This step reloads the switch IP
    driver.get('https://10.10.10.10')
    
    #Below two steps send username/password and wait 13 sec
    actions.send_keys('username', Keys.TAB).perform()
    actions.send_keys('password', Keys.ENTER).perform()
    time.sleep(13)
    
    #After log in, these 3 steps do a click on "Save Button" on the left, wait 3 seconds and select "Yes" when asked to save configuration
    driver.find_element(By.ID, 'saveConfigButton').click()
    time.sleep(3)
    driver.find_element(By.ID, 'button-1006').click()
    
    #This step does a click on "Refresh" button
    driver.find_element(By.ID, 'refreshButton-btnEl').click()
    
    #Below 3 steps are used to click on port 1, and then clicks on two buttons: "Edit" and "Graph"
    driver.find_element(By.ID, 'Port_193').click()
    driver.find_element(By.ID, 'editButton').click()
    driver.find_element(By.ID, 'graphButton-btnIconEl').click()
    
    #These 4 steps are used to click on "Help Setup Guide" button(which opens a new tab), go back to initial tab and wait 3sec
    driver.find_element(By.ID, 'helpButton-btnIconEl').click()
    original_window = driver.current_window_handle
    driver.switch_to.window(original_window)
    time.sleep(3)
    
    #These 3 steps are used to click on "Help Documentation" button(which opens a new tab), go back to initial tab and wait 3sec
    driver.find_element(By.ID, 'helpDocumentationButton').click()
    driver.switch_to.window(original_window)
    time.sleep(3)
    
    #Below 7 steps are used to click in the search text field, search for "chassis" and click on it.
    driver.find_element(By.ID, 'trigger-1023-inputEl').click()
    actions.send_keys('chassis')
    actions.perform()
    time.sleep(5)
    driver.find_element(By.ID, 'treeview-1014-record-editChassis').click()
    actions.perform()
    time.sleep(2)
    
    #Below 4 steps are used to search if right build version is present on the box and making a screenshot of the whole screen.
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('8.10.4.0_B009')
    pyautogui.hotkey('Return')
    pyautogui.screenshot('8.10.4.0_B009.png')
