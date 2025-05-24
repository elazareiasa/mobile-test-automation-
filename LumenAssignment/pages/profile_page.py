from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_name_accessibility_id = "Peter Pan"

    def is_loaded(self, timeout=10):
        try:
            profile_name_elem = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, self.profile_name_accessibility_id)
                )
            )
            return profile_name_elem.is_displayed()
        except TimeoutException:
            return False