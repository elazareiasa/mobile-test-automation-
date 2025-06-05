from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.messages_page import MessagesPage
from pages.profile_page import ProfilePage

class Tabs:
    TAB_ACCESSIBILITY_IDS = {
        "home": "Home\nTab 1 of 3",
        "messages": "Messages\nTab 2 of 3",
        "profile": "Profile\nTab 3 of 3",
    }

    PAGE_CLASSES = {
        "home": HomePage,
        "messages": MessagesPage,
        "profile": ProfilePage,
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

        page_class = self.PAGE_CLASSES.get(tab_name)
        if page_class is None:
            raise ValueError(f"Unknown tab name '{tab_name}'")
        return page_class(self.driver)
