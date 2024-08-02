# project/tests/test_deposit_page.py

import pytest
from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestDepositPage(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.login_page = self.home_page.click_customer_login()
        self.main_page = self.login_page.login_user("Harry Potter")
        self.test_deposit_amount = "100"
        self.expected_balance_after_deposit = "100"

    def test_deposit_amount_and_validate_balance(self):
        self.main_page.click_deposit()
        self.main_page.enter_amount_and_confirm(self.test_deposit_amount, "Deposit Successful")
        new_balance = self.main_page.get_balance()
        assert new_balance == self.expected_balance_after_deposit, f"Expected new balance '{self.expected_balance_after_deposit}' but got '{new_balance}'"
