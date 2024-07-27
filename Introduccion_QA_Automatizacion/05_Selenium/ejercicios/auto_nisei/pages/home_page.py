from pages.login_page import LoginPage
from pages.base_page_with_header import BasePageWithHeader

class HomePage(BasePageWithHeader):
    """
    HomePage represents the landing page after a successful login.
    It includes methods to perform actions specific to the home page.
    """
    def login_with_credentials(self, username, email, password):
        """
        Log in with the provided credentials.
        Redirects to the login page, performs login, and checks for success.
        """
        self.click_login(username)
        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        if login_page.is_login_successful():
            return self
        else:
            raise Exception("Login failed")

    def is_home_page_loaded(self):
        """
        Verify that the home page has loaded by checking for specific elements.
        This can include verifying the presence of elements unique to the home page.
        """
        # Add checks specific to HomePage
        pass
