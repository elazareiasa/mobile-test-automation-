from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @property
    def email_input(self):
        return self.wait.until(
            lambda d: d.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        )[0]

    @property
    def password_input(self):
        return self.wait.until(
            lambda d: d.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        )[1]

    @property
    def login_button(self):
        return self.wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button"))
        )

    def wait_for_editable(self, element, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: element.is_enabled() and element.get_attribute("focused") == "true"
        )

    def enter_credentials(self, email, password):
        self.wait.until(EC.element_to_be_clickable(self.email_input)).click()
        self.wait_for_editable(self.email_input)
        self.email_input.send_keys(email)

        self.wait.until(EC.element_to_be_clickable(self.password_input)).click()
        self.wait_for_editable(self.password_input)
        self.password_input.send_keys(password)

    def tap_login(self):
        self.login_button.click()

    def get_welcome_message(self, expected_email):
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, f"Welcome {expected_email}"))
        )
