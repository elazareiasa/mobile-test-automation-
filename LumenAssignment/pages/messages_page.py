import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MessagesPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self, timeout=10):
        try:
            message_container = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().className("android.view.View").instance(7)'
        )
            return message_container.is_displayed()
        except TimeoutException:
            return False