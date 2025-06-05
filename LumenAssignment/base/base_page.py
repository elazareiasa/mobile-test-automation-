from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element(self, locator, index=0):
        return self.wait.until(
            lambda d: d.find_elements(*locator))[index]

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def wait_for_editable(self, element, timeout=10):
        self.wait.until(EC.element_to_be_clickable(element)).click()
        WebDriverWait(self.driver, timeout).until(
            lambda d: element.is_enabled() and element.get_attribute("focused") == "true"
    )

    def enter_text(self, locator, text, index=0):
        element = self.wait_for_element(locator, index)
        self.wait_for_editable(element)
        element.send_keys(text)

    def is_element_displayed(self, locator, index=0):
        try:
            return self.wait_for_element(locator, index).is_displayed()
        except:
            return False
