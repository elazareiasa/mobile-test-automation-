import pytest
from pages.login_page import LoginPage

@pytest.mark.login_credentials(user="admin")
def test_home_screen_after_login(driver, current_user):
    login_page = LoginPage(driver)
    
    assert login_page.is_welcome_message_displayed(current_user["username"])

@pytest.mark.login_credentials(user="invalid")
def test_login_failure_empty_password(driver, current_user):
    login_page = LoginPage(driver)

    driver.save_screenshot("login_failed_empty_password.png")

    assert not login_page.is_welcome_message_displayed(current_user["username"]), \
        "Login should not succeed with empty password"