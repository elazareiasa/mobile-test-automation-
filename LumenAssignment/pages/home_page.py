from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    COUNTER_ACCESSIBILITY_ID = "0"

    def __init__(self, driver):
        self.driver = driver

    def get_counter_value(self, app_state):
        # expected_count = 1
        counter_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{app_state["count"]}")')
        counter_element = self.driver.find_element(*counter_locator)

        return counter_element.get_attribute("content-desc")
    
    def reset_counter(self, app_state):
        wait = WebDriverWait(self.driver, 10)
        reset_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Reset Counter"))
        )
        reset_button.click()
        app_state["count"] = 0