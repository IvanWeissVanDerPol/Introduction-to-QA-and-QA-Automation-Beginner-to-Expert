# project/tests/test_full_workflow.py

import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestFullWorkflow(BaseTest):

    def test_full_workflow(self):
        login_page = self.homepage.click_customer_login()
        main_page = login_page.login_user("Harry Potter")

        user_name = main_page.get_user_name()
        assert user_name == "Harry Potter", f"Expected user name 'Harry Potter' but got '{user_name}'"

        balance = main_page.get_balance()
        account_number = main_page.get_selected_account()
        currency = main_page.get_currency()

        assert account_number == "1004", f"Expected account number '1004' but got '{account_number}'"
        assert balance == "0", f"Expected balance '0' but got '{balance}'"
        assert currency == "Dollar", f"Expected currency 'Dollar' but got '{currency}'"
