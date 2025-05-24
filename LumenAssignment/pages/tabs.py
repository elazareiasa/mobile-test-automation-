from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tabs:
    TAB_ACCESSIBILITY_IDS = {
        "home": "Home\nTab 1 of 3",
        "messages": "Messages\nTab 2 of 3",
        "profile": "Profile\nTab 3 of 3",
    }

    def __init__(self, driver, app_state):
        self.driver = driver
        self.expected_count = app_state

    def go_to(self, tab_name):
        wait = WebDriverWait(self.driver, 10)

        tab_id = self.TAB_ACCESSIBILITY_IDS[tab_name]
        tab_element = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, tab_id))
        )
        tab_element.click()
        self.expected_count["count"] += 1
