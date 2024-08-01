# project/tests/test_withdraw_page.py

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestWithdrawPage(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """
        Sets up the required pages and initial values for the tests.
        """
        self.home_page = HomePage(self.driver)
        self.login_page = self.home_page.click_customer_login()
        self.main_page = self.login_page.login_user("Harry Potter")
        self.test_deposit_amount = "100"
        self.expected_balance_after_withdraw = "0"
        
    def test_withdraw_amount_and_validate_balance(self):
        """
        Tests withdrawing a valid amount and validates the balance.
        """
        assert self.main_page.get_balance() == "0", "Initial balance is not 0"
        
        self.main_page.click_deposit()
        self.main_page.enter_amount_and_confirm(self.test_deposit_amount, "Deposit Successful")
        
        self.main_page.click_withdraw()
        self.main_page.enter_amount_and_confirm(self.test_deposit_amount, "Transaction successful")
        
        assert self.main_page.get_balance() == self.expected_balance_after_withdraw, f"Expected balance '{self.expected_balance_after_withdraw}' but got '{self.main_page.get_balance()}'"

    def test_withdraw_more_than_we_have(self):
        """
        Tests withdrawing more than the available balance and validates the error message.
        """
        balance = self.main_page.get_balance()
        self.main_page.click_withdraw()
        self.main_page.enter_amount_and_confirm(str(int(balance) + 100), "Transaction Failed. You can not withdraw amount more than the balance.")
