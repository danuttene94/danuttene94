#Details about this script are in Readme.md file

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username").send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password").send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']").click()

        # Scroll down to log in process
        iframe = driver.find_element(By.CLASS_NAME, "wp-block-separator")
        ActionChains(driver) \
            .scroll_to_element(iframe) \
            .perform()

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_message_text = error_message.text
        assert error_message_text == expected_error_message, "Error message is not expected"

