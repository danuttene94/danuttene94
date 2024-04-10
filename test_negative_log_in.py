#The purpose of this script is written in README.md file


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
print(driver.service.is_connectable())  # print True
action = ActionChains(driver)
driver.implicitly_wait(5)


def test_edm_login_negative():
    #This step opens the switch IP
    driver.get('https://10.10.10.10')

    #These two steps below help passing over the security warning
    driver.find_element(By.XPATH, '//button[@class="secondary-button small-link"]').click()
    driver.find_element(By.ID, 'proceed-link').click()

    #This step reloads the switch IP
    driver.get('https://10.10.10.10')

    #Below three steps send username and wrong password, waits 13 sec
    actions.send_keys('username', Keys.TAB).perform()
    actions.send_keys('wrongpassword', Keys.ENTER)
    actions.perform()

    #Below steps are used to search for "Authentification Failed" text which is shown when the wrong password is inserted, after a screenshot is made of the whole screen
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('Authentication Failed')
    pyautogui.hotkey('Return')
    pyautogui.screenshot('negative test.png')
    time.sleep(5)
