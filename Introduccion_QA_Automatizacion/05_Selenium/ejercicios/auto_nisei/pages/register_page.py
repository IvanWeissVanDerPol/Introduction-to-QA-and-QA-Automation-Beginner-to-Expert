from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class RegisterPage(BasePageWithHeader):
    USERNAME_FIELD = (By.ID, "username")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "confirm_password")
    SUBMIT_BUTTON = (By.ID, "submit")
    GOOGLE_SIGNUP_BUTTON = (By.CSS_SELECTOR, "button.google-signup")

    def register_with_credentials(self, username, email, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.enter_text(self.CONFIRM_PASSWORD_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)

    def register_with_google(self, email, password):
        self.click_element(self.GOOGLE_SIGNUP_BUTTON)
        main_window = self.switch_to_google_auth_window()
        self.google_authenticate(email, password)
        self.driver.switch_to.window(main_window)

    def switch_to_google_auth_window(self):
        # Switch to the Google authentication window
        main_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return main_window

    def google_authenticate(self, email, password):
        EMAIL_FIELD = (By.ID, "identifierId")
        NEXT_BUTTON = (By.ID, "identifierNext")
        PASSWORD_FIELD = (By.NAME, "password")
        LOGIN_BUTTON = (By.ID, "passwordNext")

        self.enter_text(EMAIL_FIELD, email)
        self.click_element(NEXT_BUTTON)

        self.wait_for_element(PASSWORD_FIELD, timeout=20)
        self.enter_text(PASSWORD_FIELD, password)
        self.click_element(LOGIN_BUTTON)
