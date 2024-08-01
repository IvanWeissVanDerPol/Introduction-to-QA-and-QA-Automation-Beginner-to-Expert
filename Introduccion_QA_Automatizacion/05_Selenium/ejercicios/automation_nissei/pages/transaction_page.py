# project/pages/transaction_page.py

from pages.base_page import BasePage
from utils.locator import TransactionPageLocators
import logging
from selenium.webdriver.common.by import By

class TransactionPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the TransactionPage with the given WebDriver instance.
        """
        super().__init__(driver)

    def select_account(self, account_number):
        """
        Selects an account from the dropdown by visible text.
        Logs the action.
        """
        logging.info(f"Selecting account number {account_number}")
        select = self.find_element(TransactionPageLocators.ACCOUNT_SELECT)
        for option in select.find_elements(By.TAG_NAME, 'option'):
            if option.text == str(account_number):
                option.click()
                logging.info(f"Selected account number {account_number}")
                break

    def click_transactions(self):
        """
        Clicks the transactions button.
        Logs the action.
        """
        logging.info("Clicking on Transactions button")
        self.click_element(TransactionPageLocators.TRANSACTIONS_BUTTON)

    def click_deposit(self):
        """
        Clicks the deposit button.
        Logs the action.
        """
        logging.info("Clicking on Deposit button")
        self.click_element(TransactionPageLocators.DEPOSIT_BUTTON)

    def click_withdraw(self):
        """
        Clicks the withdraw button.
        Logs the action.
        """
        logging.info("Clicking on Withdraw button")
        self.click_element(TransactionPageLocators.WITHDRAW_BUTTON)
