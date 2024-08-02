# project/tests/test_home_page.py

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest
import logging
from utils.locator import HomePageLocators

@pytest.mark.usefixtures("setup")
class TestHomePage(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """
        Sets up the required pages and initial values for the tests.
        """
        self.home_page = HomePage(self.driver)

    def test_home_button(self):
        home_button = self.homepage.find_element(HomePageLocators.HOME_BUTTON)
        assert home_button.is_displayed(), "Home button is not visible"
        self.homepage.click_home()

    
    def test_customer_login_button(self):
        customer_login_button = self.homepage.find_element(HomePageLocators.CUSTOMER_LOGIN_BUTTON)
        assert customer_login_button.is_displayed(), "Customer Login button is not visible"
        self.homepage.click_customer_login()
        self.homepage.verify_current_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")

    
    def test_bank_manager_login_button(self):
        manager_login_button = self.homepage.find_element(HomePageLocators.MANAGER_LOGIN_BUTTON)
        assert manager_login_button.is_displayed(), "Bank Manager Login button is not visible"
        self.homepage.click_manager_login()
        self.homepage.verify_current_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager")


