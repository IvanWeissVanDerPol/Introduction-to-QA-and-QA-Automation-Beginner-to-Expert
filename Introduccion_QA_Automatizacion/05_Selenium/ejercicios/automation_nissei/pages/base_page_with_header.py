import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage

class BasePageWithHeader(BasePage):
    """
    BasePageWithHeader extends BasePage to include common elements found in the header
    of most pages. This helps to reduce redundancy in our page models.
    """
    REGISTER_BUTTON = (By.LINK_TEXT, "Registrarme")
    LOGIN_BUTTON = (By.LINK_TEXT, "Iniciar sesión")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, "a.wishlist-icon.link.wishlist")
    CART_BUTTON = (By.CSS_SELECTOR, "a.action.showcart")
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.action.search")
    ACCOUNT_MENU = (By.CSS_SELECTOR, "div.user-topbar.col")
    ACCOUNT_LINK = (By.LINK_TEXT, "Mi Cuenta")
    ORDERS_LINK = (By.LINK_TEXT, "Mis pedidos")
    WISHLIST_LINK = (By.LINK_TEXT, "Mi lista de deseos")
    CART_LINK = (By.LINK_TEXT, "Mi carrito")
    LOGOUT_LINK = (By.LINK_TEXT, "Cerrar sesión")

    def click_register(self):
        """
        Click the register button if the user is not logged in.
        Ensures that the user is taken to the registration page.
        """
        if not self.is_user_logged_in():
            self.click_element(self.REGISTER_BUTTON)
        else:
            logging.info("You are already logged in. Please log out to register.")

    def click_login(self, username):
        """
        Click the login button if the user is not logged in.
        Initiates the login process.
        """
        if not self.is_user_logged_in(username):
            self.click_element(self.LOGIN_BUTTON)
        else:
            logging.info("You are already logged in. No need to log in again.")

    def click_wishlist(self):
        """
        Click the wishlist button to navigate to the wishlist page.
        """
        self.click_element(self.WISHLIST_BUTTON)

    def click_cart(self):
        """
        Click the cart button to navigate to the shopping cart.
        """
        self.click_element(self.CART_BUTTON)

    def enter_search_term(self, term):
        """
        Enter a search term into the search field.
        """
        self.enter_text(self.SEARCH_FIELD, term)

    def submit_search(self):
        """
        Submit the search form.
        """
        self.click_element(self.SEARCH_BUTTON)

    def click_account_link(self):
        """
        Click the account link if the user is logged in.
        """
        self._click_if_logged_in(self.ACCOUNT_LINK)

    def click_orders_link(self):
        """
        Click the orders link if the user is logged in.
        """
        self._click_if_logged_in(self.ORDERS_LINK)

    def click_wishlist_link(self):
        """
        Click the wishlist link if the user is logged in.
        """
        self._click_if_logged_in(self.WISHLIST_LINK)

    def click_cart_link(self):
        """
        Click the cart link if the user is logged in.
        """
        self._click_if_logged_in(self.CART_LINK)

    def click_logout_link(self):
        """
        Click the logout link if the user is logged in.
        """
        self._click_if_logged_in(self.LOGOUT_LINK)

    def _click_if_logged_in(self, locator, username):
        """
        Click an element if the user is logged in.
        This ensures that only logged-in users can access certain pages.
        """
        if self.is_user_logged_in(username):
            self.click_element(locator)
        else:
            logging.info("You need to be logged in to access this page.")

    def is_user_logged_in(self, username):
        """
        Check if the user is logged in by looking for their username in the account menu.
        """
        try:
            account_menu = self.wait_for_element(self.ACCOUNT_MENU, timeout=5)
            name_element = self.driver.find_element(By.CSS_SELECTOR, "div.name")
            if account_menu and name_element.text == username:
                return True
        except Exception:
            return False
