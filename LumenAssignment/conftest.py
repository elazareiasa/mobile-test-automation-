import os
import pytest
import yaml
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage

def load_users():
    config_path = os.path.join(os.path.dirname(__file__), "config", "users.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)["users"]

@pytest.fixture(scope="session")
def user_data():
    return load_users()

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = os.getenv("DEVICE_NAME", "emulator-5554")
    options.automation_name = "UiAutomator2"
    options.app_package = "com.example.mycounter.mycounter"
    # options.app = os.path.abspath("path/to/app.apk")
    options.set_capability("adbExecTimeout", 3000000)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def login(request, driver, user_data):
    login_page = LoginPage(driver)

    user_key = "admin"

    marker = request.node.get_closest_marker("login_credentials")
    if marker:
        user_key = marker.kwargs.get("user", "admin")

    user = user_data.get(user_key)

    if not user:
        pytest.skip(f"User '{user_key}' not found in users.yaml")

    login_page.enter_credentials(user["username"], user["password"])
    login_page.tap_login()

    return driver

@pytest.fixture(scope="session")
def app_state():
    state = {"count": 0}
    yield state

@pytest.fixture
def current_user(request, user_data):
    marker = request.node.get_closest_marker("login_credentials")
    user_key = marker.kwargs.get("user", "admin") if marker else "admin"
    return user_data.get(user_key)
