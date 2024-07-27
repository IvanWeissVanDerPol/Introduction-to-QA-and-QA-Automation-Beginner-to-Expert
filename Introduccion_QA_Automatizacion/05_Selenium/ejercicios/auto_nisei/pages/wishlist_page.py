from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class WishlistPage(BasePageWithHeader):
    WISHLIST_ICON = (By.CSS_SELECTOR, "a.wishlist-icon.link.wishlist")
    WISHLIST_COUNTER = (By.CSS_SELECTOR, "span.counter-number.qty")

    def open_wishlist(self):
        self.click_element(self.WISHLIST_ICON)

    def get_wishlist_count(self):
        return self.wait_for_element(self.WISHLIST_COUNTER).text
