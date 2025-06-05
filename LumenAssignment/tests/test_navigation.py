import pytest
from pages.tabs import Tabs

@pytest.mark.login_credentials(user="admin")
def test_tab_navigation(driver, app_state):
    tabs = Tabs(driver, app_state)

    home_page = tabs.go_to("home")
    assert int(home_page.get_counter_value(app_state)) == app_state["count"]

    messages_page = tabs.go_to("messages")
    assert messages_page.is_loaded()

    profile_page = tabs.go_to("profile")
    assert profile_page.is_loaded()

    tabs.go_to("home")
    assert int(home_page.get_counter_value(app_state)) == app_state["count"]

    home_page.reset_counter(app_state)

    assert int(home_page.get_counter_value(app_state)) == 0
