1. The purpose of "test_positive_login.py" is to save time, at each new release we must do a regression testing on the WEB interface of the switch. Better said, we have to log in using the switch IP, pass over a security warnining, check if the 5 main buttons work as expected. I also added a search&screenshot at the end to search for the release we need.

2. The purpose of "test_negative_log_in.py" is an addition for the test_positive_login.py, just to check if you can log in the WEB interface of the switch with a wrong password.

3. The purpose of "Login_and_checks_test.py" is to do a log in on a test page and a few checks that the link is correct and given text is found on the page.

4. The purpose of "Temperature_test.py" is to do a Log in on the switch web management interface, go to "System Temperature" menu and do a screenshot of the page. This option was used because the box that contained the temperature number is not selectable so i couldn't find the element and do an assert on the text.

5. Files "test_login_page_positive.py", " test_login_page_negative.py", "test_exceptions.py", "conftest.py", "pytest.ini" were developed during the "Selenium WebDriver: Selenium Automation Testing with Python", by Dmitry Shyshkin on Udemy.
   Here i learned more advanced topics on Selenium/Python and how to create a framework, such as: Pytest, marks, fixtures, parametrization, implicit/explicit waits,     how to run multiple tests at once or using multiple browsers at once and also test some of the most common exceptions.
