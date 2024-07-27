from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class CartPage(BasePageWithHeader):
    CART_ICON = (By.CSS_SELECTOR, "a.action.showcart")
    CART_COUNTER = (By.CSS_SELECTOR, "span.counter-number")

    def open_cart(self):
        self.click_element(self.CART_ICON)

    def get_cart_count(self):
        return self.wait_for_element(self.CART_COUNTER).text
