from selenium.webdriver.common.by import By
from .base_page_with_header import BasePageWithHeader

class ProductPage(BasePageWithHeader):
    """
    ProductPage handles interactions with the product page elements.
    """
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart")

    def add_to_cart(self):
        """
        Click the 'Add to Cart' button to add the product to the shopping cart.
        """
        self.click_element(self.ADD_TO_CART_BUTTON)
