# project/pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from utils.utils import wait_for_page_load
import os
import time
import logging

class BasePage:
    def __init__(self, driver):
        """
        Initializes the base page with the given WebDriver instance.
        Waits for the page to load completely.
        """
        self.driver = driver
        wait_for_page_load(self.driver)
        logging.info("Page loaded successfully.")

    def find_element(self, locator, timeout=20) -> WebElement or None:
        """
        Finds a single element on the page using a given locator and timeout.
        Logs each step and handles exceptions by capturing a screenshot.
        """
        try:
            logging.info(f"Trying to find element by {locator[0]} with value {locator[1]}")
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator[0], locator[1])))
            logging.info(f"Element found: {locator[0]} with value {locator[1]}")
            return element
        except Exception as e:
            logging.error(f"Error finding element by {locator[0]} with value {locator[1]}: {e}")
            self.capture_screenshot(f"error_{locator[0]}_{locator[1]}")
            return None
        
    def find_elements(self, locator, timeout=20) -> list[WebElement] or None:
        """
        Finds multiple elements on the page using a given locator and timeout.
        Logs each step and handles exceptions by capturing a screenshot.
        """
        try:
            logging.info(f"Trying to find elements by {locator[0]} with value {locator[1]}")
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator[0], locator[1])))
            logging.info(f"Elements found: {locator[0]} with value {locator[1]}")
            return elements
        except Exception as e:
            logging.error(f"Error finding elements by {locator[0]} with value {locator[1]}: {e}")
            self.capture_screenshot(f"error_{locator[0]}_{locator[1]}")
            return []

    def click_element(self, locator, timeout=20):
        """
        Clicks on an element located by a given locator and timeout.
        Logs each step and handles exceptions.
        """
        logging.info(f"Attempting to click element by {locator[0]} with value {locator[1]}")
        element = self.find_element(locator, timeout)
        if element:
            element.click()
            logging.info(f"Clicked element by {locator[0]} with value {locator[1]}")
        else:
            logging.error(f"Failed to click element by {locator[0]} with value {locator[1]}")

    def enter_text(self, locator, text, timeout=20):
        """
        Enters text into an input field located by a given locator and timeout.
        Logs each step and handles exceptions.
        """
        logging.info(f"Attempting to enter text into element by {locator[0]} with value {locator[1]}")
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text '{text}' into element by {locator[0]} with value {locator[1]}")
        else:
            logging.error(f"Failed to enter text into element by {locator[0]} with value {locator[1]}")

    def capture_screenshot(self, name="screenshot"):
        """
        Captures a screenshot and saves it with a timestamped filename.
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to {screenshot_path}")
