from pages.login_page import LoginPage
from pages.base_page_with_header import BasePageWithHeader

class HomePage(BasePageWithHeader):
   
    def login_with_credentials(self, username, email, password):
        self.click_login(username)
        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        return self


    