import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = os.getenv("DEVICE_NAME")
    options.automation_name = "UiAutomator2"
    options.app = os.getenv("APP_PATH")
    options.set_capability("adbExecTimeout", 3000000)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    login_page.enter_credentials("test@lumen.me", "qwerty")
    login_page.tap_login()
    return driver

@pytest.fixture(scope="session")
def app_state():
    state = {"count": 0}
    yield state
