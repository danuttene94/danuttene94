#Details about this script are in Readme.md file

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Testexceptions:

    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find/Click "Add" button
        add_button_locator = driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        assert row2_input_element.is_displayed(), "Row2 should be displayed, but it's not"

    def test_not_interactable_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn").click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row2_input_element.send_keys("Sushi")

        # Push Save button using locator By.name(“Save”)
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # Verify text was saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_element = confirmation_element.text
        assert confirmation_element == "Row 2 was saved", "Confirmation message is not expected"

    def test_stale_element_reference_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        instructions_element = driver.find_element(By.ID, "instructions")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        assert not instructions_element.is_displayed(), "Instruction message should not be displayed"


    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        edit_button = driver.find_element(By.ID, "edit_btn")
        edit_button.click()
        row1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input[@type='text']")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row1_input_element))
        row1_input_element.clear()

        # Type text into the input field
        row1_input_element.send_keys("Sushi")
        row1_save_button = driver.find_element(By.ID, "save_btn").click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"


    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn").click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instruction element should not be displayed")

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input"))
                                        , "Failed waiting for Row 2 input to be visible")

        # Verify second input field is displayed
        assert row2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
