import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configure logging to capture debug information
logging.basicConfig(level=logging.INFO)

class BasePage:
    def __init__(self, driver):
        """
        Base page class that all page models can inherit from.
        Initializes the driver for use in all methods.
        """
        self.driver = driver

    def open_base_url(self, url):
        """
        Open the specified URL.
        This is typically the starting point of a test.
        """
        logging.info(f"Opening URL: {url}")
        self.driver.get(url)

    def get_page_title(self):
        """
        Return the title of the current page.
        Useful for assertions to ensure the correct page is loaded.
        """
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for an element to be visible within the specified timeout.
        This ensures that the element is loaded and interactable.
        """
        logging.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        """
        Click on the specified element.
        This method uses wait_for_element to ensure the element is ready for interaction.
        """
        try:
            element = self.wait_for_element(locator, timeout)
            element.click()
            logging.info(f"Clicked element: {locator}")
        except Exception as e:
            logging.error(f"Error clicking element {locator}: {e}")
            raise

    def enter_text(self, locator, text, timeout=10):
        """
        Enter text into the specified element.
        Clears any existing text before entering new text to avoid input errors.
        """
        try:
            element = self.wait_for_element(locator, timeout)
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text into element: {locator}")
        except Exception as e:
            logging.error(f"Error entering text into element {locator}: {e}")
            raise

    def submit_form(self, locator, timeout=10):
        """
        Submit the form by locating the specified element.
        """
        try:
            element = self.wait_for_element(locator, timeout)
            element.submit()
            logging.info(f"Submitted form: {locator}")
        except Exception as e:
            logging.error(f"Error submitting form {locator}: {e}")
            raise

    def close_onesignal_popup(self):
        """
        Close the OneSignal popup if it appears.
        This is a common popup that can interfere with test flows.
        """
        try:
            logging.info("Closing OneSignal popup if present.")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "onesignal-slidedown-container"))
            )
            no_gracias_button = self.driver.find_element(By.ID, "onesignal-slidedown-cancel-button")
            no_gracias_button.click()
        except Exception as e:
            logging.warning(f"Pop-up did not appear or could not be closed: {e}")
