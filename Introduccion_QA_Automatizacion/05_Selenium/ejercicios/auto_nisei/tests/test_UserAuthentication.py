import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from .test_BaseTest import BaseTest

@pytest.mark.usefixtures("setup")
class TestAuthSuite(BaseTest):

    @pytest.mark.parametrize("username, email, password", [
        ("Fake", "fakemailpoli@gmail.com", "FakeMail123!"),
    ])
    def test_login_with_credentials(self, username, email, password, config):
        home_page = HomePage(self.driver)
        home_page.open_base_url(config["base_url"])
        home_page.close_onesignal_popup()
        
        assert "Nissei" in home_page.get_page_title()

        home_page.login_with_credentials(username, email, password)

        import time
        time.sleep(60)  # Wait for 1 minute
        # Check if the user is logged in
        assert home_page.is_user_logged_in(username)