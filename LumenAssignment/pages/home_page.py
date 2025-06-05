from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class HomePage(BasePage):
    COUNTER_ACCESSIBILITY_ID = "0"

    def __init__(self, driver):
        super().__init__(driver)
        self.reset_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Reset Counter")


    def get_counter_value(self, app_state):
        counter_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{app_state["count"]}")')
        counter_element = self.wait_for_element(counter_locator)

        return counter_element.get_attribute("content-desc")
    
    def reset_counter(self, app_state):
        reset_button = self.wait_for_element(self.reset_button_locator)
        reset_button.click()
        app_state["count"] = 0