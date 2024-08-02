# project/utils/utils.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def wait_for_page_load(driver, timeout=20):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

def wait_for_element(driver, by, value, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

def login_user(driver, username):
    from pages.home_page import HomePage  # Local import to avoid circular import
    from pages.login_page import LoginPage  # Local import to avoid circular import

    logging.info(f"Logging in user: {username}")
    homepage = HomePage(driver)
    homepage.click_customer_login()
    logging.info("Navigated to Customer Login page")
    login_page = LoginPage(driver)
    login_page.login_user(username)
    logging.info(f"User {username} logged in successfully")
