# project/pages/login_page.py

from pages.base_page import BasePage
from utils.locator import LoginPageLocators
import logging
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

class LoginPage(BasePage):
    def __init__(self, driver):
        """
        Initializes the LoginPage with the given WebDriver instance.
        """
        super().__init__(driver)

    def select_user(self, user_name):
        """
        Selects a user from the dropdown by text.
        Logs the selection.
        """
        user_dropdown = self.find_element(LoginPageLocators.USER_SELECT)
        for option in user_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == user_name:
                option.click()
                logging.info(f"Selected user {user_name} from dropdown")
                break

    def select_user_by_index(self, index):
        """
        Selects a user from the dropdown by index.
        Logs the selection.
        """
        user_dropdown = self.find_element(LoginPageLocators.USER_SELECT)
        options = user_dropdown.find_elements(By.TAG_NAME, 'option')
        if 0 <= index < len(options):
            options[index].click()
            logging.info(f"Selected user {options[index].text} from dropdown")
        else:
            logging.error(f"Index {index} is out of range for user dropdown options")

    def click_login_button(self):
        """
        Clicks the login button.
        Logs the action.
        """
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        logging.info("Clicked login button")

    def login_user(self, user_name):
        """
        Logs in a user by selecting the username from a dropdown and clicking login.
        Returns the MainPage object.
        """
        self.select_user(user_name)
        self.click_login_button()
        logging.info(f"Logged in user {user_name}")
        return MainPage(self.driver)

    def select_user_and_login(self, index):
        """
        Selects a user by index from the dropdown and clicks the login button.
        """
        self.select_user_by_index(index)
        self.click_login_button()

    def verify_user_dropdown_options(self):
        """
        Verifies the visibility of the user dropdown and its options.
        """
        user_dropdown = self.find_element(LoginPageLocators.USER_SELECT)
        assert user_dropdown.is_displayed(), "User Dropdown is not visible"

        options = user_dropdown.find_elements(By.TAG_NAME, 'option')
        for option in options:
            user_dropdown.click()
            option.click()
            selected_option = user_dropdown.find_element(By.CSS_SELECTOR, 'option:checked')
            assert selected_option.text == option.text, "Selected text is not displayed in the dropdown"
