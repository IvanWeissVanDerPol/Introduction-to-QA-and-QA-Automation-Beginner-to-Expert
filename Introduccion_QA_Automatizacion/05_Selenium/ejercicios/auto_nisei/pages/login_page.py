from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class LoginPage(BasePageWithHeader):
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    SUBMIT_BUTTON = (By.ID, "send2")

    def login(self, email, password):
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)
