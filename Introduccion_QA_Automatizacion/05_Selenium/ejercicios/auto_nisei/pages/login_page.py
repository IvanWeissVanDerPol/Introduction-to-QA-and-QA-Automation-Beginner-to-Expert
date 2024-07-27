from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class LoginPage(BasePageWithHeader):
    """
    LoginPage handles the login process by interacting with the email, password,
    and submit button elements on the login page.
    """
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    SUBMIT_BUTTON = (By.ID, "send2")
    ERROR_MESSAGE = (By.ID, "error-message-id")  # Example error message locator

    def login(self, email, password):
        """
        Log in using the provided email and password.
        """
        self.clear_and_enter_text(self.EMAIL_FIELD, email)
        self.clear_and_enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)

    def clear_and_enter_text(self, locator, text):
        """
        Clear the text field and enter new text.
        This ensures no residual text interferes with the input.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def is_login_successful(self):
        """
        Check if the login was successful by looking for the absence of an error message.
        This method can be expanded to include other checks if necessary.
        """
        try:
            error_message = self.driver.find_element(*self.ERROR_MESSAGE)
            return False
        except Exception:
            return True
