from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        self.password_input = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        self.login_button = (AppiumBy.CLASS_NAME, "android.widget.Button")

    def enter_credentials(self, username, password):
        self.enter_text(self.email_input, username)
        self.enter_text(self.password_input, password, 1)

    def tap_login(self):
        self.click(self.login_button)

    def get_welcome_message(self, username):
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"Welcome {username}"))
        )
    
    def is_welcome_message_displayed(self, username, timeout=10):
        welcome_locator = (AppiumBy.ACCESSIBILITY_ID, f"Welcome {username}")
        return self.is_element_displayed(welcome_locator)
