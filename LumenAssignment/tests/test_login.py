import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

USER_NAME = "test@lumen.me"

def test_home_screen_after_login(login):
    driver = login
    welcome_message = f"Welcome {USER_NAME}"
    element = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, welcome_message)
    )
    assert element.is_displayed()

def test_login_failure_empty_password(driver):
    login_page = LoginPage(driver)
    
    login_page.email_input.click()
    login_page.wait_for_editable(login_page.email_input)
    login_page.email_input.send_keys(USER_NAME)

    login_page.tap_login()

    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")) >= 2
    )

    driver.save_screenshot("login_failed_empty_password.png")

    elements = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, f"Welcome {USER_NAME}")
    assert len(elements) == 0, "Login should not succeed with empty password"