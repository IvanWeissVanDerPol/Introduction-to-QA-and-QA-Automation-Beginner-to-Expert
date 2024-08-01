# project/pages/main_page.py

import time
from pages.base_page import BasePage
from utils.locator import MainPageLocators
import logging
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the MainPage with the given WebDriver instance.
        """
        super().__init__(driver)

    def get_result_message(self):
        """
        Retrieves the result message displayed on the main page.
        Logs the action.
        """
        logging.info("Getting result message")
        return self.find_element(MainPageLocators.RESULT_MESSAGE).text

    def get_user_name(self):
        """
        Retrieves the user name displayed on the main page.
        Logs the action.
        """
        logging.info("Getting user name")
        return self.find_element(MainPageLocators.USER_NAME).text

    def get_selected_account(self):
        """
        Retrieves the selected account number from the account number dropdown.
        Logs the action.
        """
        logging.info("Getting selected account number")
        account_select = Select(self.find_element(MainPageLocators.ACCOUNT_SELECT))
        return account_select.first_selected_option.text

    def get_balance(self):
        """
        Retrieves the account balance displayed on the main page.
        Logs the action.
        """
        logging.info("Getting balance")
        return self.find_element(MainPageLocators.BALANCE).text

    def get_currency(self):
        """
        Retrieves the currency type displayed on the main page.
        Logs the action.
        """
        logging.info("Getting currency")
        return self.find_element(MainPageLocators.CURRENCY).text

    def click_home(self):
        """
        Clicks the home button.
        Logs the action.
        """
        logging.info("Clicking Home button")
        self.click_element(MainPageLocators.HOME_BUTTON)

    def click_logout(self):
        """
        Clicks the logout button.
        Logs the action.
        """
        logging.info("Clicking Logout button")
        self.click_element(MainPageLocators.LOGOUT_BUTTON)
        time.sleep(5)

    def click_transactions(self):
        """
        Clicks the transactions button.
        Logs the action.
        """
        logging.info("Clicking Transactions button")
        self.click_element(MainPageLocators.TRANSACTIONS_BUTTON)
        time.sleep(5)

    def click_deposit(self):
        """
        Clicks the deposit button.
        Logs the action.
        """
        logging.info("Clicking Deposit button")
        self.click_element(MainPageLocators.DEPOSIT_BUTTON)
        time.sleep(5)

    def click_withdraw(self):
        """
        Clicks the withdraw button.
        Logs the action.
        """
        logging.info("Clicking Withdraw button")
        self.click_element(MainPageLocators.WITHDRAW_BUTTON)
        time.sleep(5)

    def select_account(self, account_number):
        """
        Selects an account from the account number dropdown.
        Logs the action.
        """
        logging.info(f"Selecting account number: {account_number}")
        select = Select(self.find_element(MainPageLocators.ACCOUNT_SELECT))
        select.select_by_visible_text(account_number)
        logging.info(f"Account number {account_number} selected")

    def enter_amount(self, amount):
        """
        Enters the amount to be deposited or withdrawn.
        Logs the action.
        """
        logging.info(f"Entering amount: {amount}")
        self.find_element(MainPageLocators.AMOUNT_INPUT_FIELD).send_keys(amount)
        logging.info(f"Amount {amount} entered")
        
    def click_confirm_deposit(self):
        """
        Clicks the confirm deposit button.
        Logs the action.
        """
        logging.info("Clicking Confirm Deposit button")
        self.click_element(MainPageLocators.CONFIRM_BUTTON)

    def click_confirm_withdraw(self):
        """
        Clicks the confirm withdraw button.
        Logs the action.
        """
        logging.info("Clicking Confirm Withdraw button")
        self.click_element(MainPageLocators.CONFIRM_BUTTON)

    def enter_amount_and_confirm(self, amount, expected_message):
        """
        Enters the amount and clicks the confirm button for deposit or withdrawal.
        Validates the success message.
        Logs all actions.
        """
        self.enter_amount(amount)
        self.click_confirm_deposit() if expected_message == "Deposit Successful" else self.click_confirm_withdraw()
        actual_message = self.get_result_message()
        assert actual_message == expected_message, f"Expected message '{expected_message}' but got '{actual_message}'"
