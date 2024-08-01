# project/tests/test_account_main_page.py

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestAccountMainPage(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.login_page = self.home_page.click_customer_login()
        self.main_page = self.login_page.login_user("Harry Potter")

        self.expected_home_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        self.expected_customer_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
        self.expected_transactions_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
        self.test_user = "Harry Potter"
        self.test_account_numbers = ["1004", "1005", "1006"]
        self.expected_currency = "Dollar"
        self.expected_innitial_balance = "0"
        

    def test_home_button_redirects_to_login(self):
        self.main_page.click_home()
        current_url = self.driver.current_url
        assert current_url == self.expected_home_url, f"Expected URL: {self.expected_home_url}, Actual URL: {current_url}"

    def test_logout_button_redirects_to_customer_login(self):
        self.main_page.click_logout()
        current_url = self.driver.current_url
        assert current_url == self.expected_customer_url, f"Expected URL: {self.expected_customer_url}, Actual URL: {current_url}"

    def test_welcome_message_displays_correct_user(self):
        user_name = self.main_page.get_user_name()
        assert user_name == self.test_user, f"Expected user name '{self.test_user}' but got '{user_name}'"

    def test_account_number_dropdown_functionality(self):
        for account_number in self.test_account_numbers:
            self.main_page.select_account(account_number)
            selected_account = self.main_page.get_selected_account()
            assert selected_account == account_number, f"Expected account number '{account_number}' but got '{selected_account}'"

    def test_balance_and_currency_visibility(self):
        balance = self.main_page.get_balance()
        currency = self.main_page.get_currency()
        assert balance == self.expected_innitial_balance, f"Expected balance '{self.expected_innitial_balance}' but got '{balance}'"
        assert currency == self.expected_currency, f"Expected currency '{self.expected_currency}' but got '{currency}'"

    def test_transactions_button_functionality(self):
        self.main_page.click_transactions()
        current_url = self.driver.current_url
        assert current_url == self.expected_transactions_url, f"Expected URL: {self.expected_transactions_url}, Actual URL: {current_url}"

