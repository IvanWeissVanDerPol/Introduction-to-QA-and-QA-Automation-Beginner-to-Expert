# project/tests/test_customer_login_page.py

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestCustomerLoginPage(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.homepage = HomePage(self.driver)
        self.login_page = self.homepage.click_customer_login()

    def test_home_button_redirects_to_login(self):
        self.homepage.click_home()
        self.homepage.verify_current_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def test_user_dropdown_functionality(self):
        self.login_page.verify_user_dropdown_options()

    def test_login_button_functionality(self):
        self.login_page.select_user_and_login(2)
        self.homepage.verify_url_changed("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
