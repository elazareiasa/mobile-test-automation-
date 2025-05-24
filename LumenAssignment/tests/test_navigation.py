from pages.home_page import HomePage
from pages.messages_page import MessagesPage
from pages.profile_page import ProfilePage
from pages.tabs import Tabs

def test_tab_navigation(login, app_state):
    driver = login
    tabs = Tabs(driver, app_state)

    tabs.go_to("home")
    home_page = HomePage(driver)
    assert int(home_page.get_counter_value(app_state)) == app_state["count"]

    tabs.go_to("messages")
    messages_page = MessagesPage(driver)
    assert messages_page.is_loaded()

    tabs.go_to("profile")
    profile_page = ProfilePage(driver)
    assert profile_page.is_loaded()

    tabs.go_to("home")
    home_page = HomePage(driver)
    assert int(home_page.get_counter_value(app_state)) == app_state["count"]

    home_page.reset_counter(app_state)

    assert int(home_page.get_counter_value(app_state)) == 0
