# project/pages/home_page.py

import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locator import HomePageLocators
import logging

class HomePage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def __init__(self, driver):
        """
        Initializes the HomePage and navigates to the URL.
        """
        super().__init__(driver)
        self.driver.get(self.URL)
        logging.info("Navigated to Home Page URL")

    def click_home(self):
        """
        Clicks the home button.
        """
        logging.info("Clicking on Home button")
        self.click_element(HomePageLocators.HOME_BUTTON)

    def verify_current_url(self, expected_url):
        """
        Verifies the current URL against the expected URL.
        """
        time.sleep(5)
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def verify_url_changed(self, previous_url):
        """
        Verifies that the current URL is different from the previous URL.
        """
        time.sleep(5)
        new_url = self.driver.current_url
        assert new_url != previous_url, "URL has not changed after login"

    def click_customer_login(self):
        """
        Clicks the customer login button and returns the LoginPage object.
        """
        logging.info("Clicking on Customer Login button")
        self.click_element(HomePageLocators.CUSTOMER_LOGIN_BUTTON)
        return LoginPage(self.driver)

    def click_manager_login(self):
        """
        Clicks the manager login button.
        """
        logging.info("Clicking on Manager Login button")
        self.click_element(HomePageLocators.MANAGER_LOGIN_BUTTON)
