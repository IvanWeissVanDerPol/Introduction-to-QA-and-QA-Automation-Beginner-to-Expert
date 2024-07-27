import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging to capture debug information
logging.basicConfig(level=logging.INFO)

def wait_for_element(driver, locator, timeout=10):
    """
    Wait for the element to be visible within the specified timeout.
    This ensures that the element is loaded and interactable.
    """
    logging.info(f"Waiting for element: {locator}")
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def click_element(driver, locator, timeout=10):
    """
    Click on the specified element.
    This method uses wait_for_element to ensure the element is ready for interaction.
    """
    try:
        element = wait_for_element(driver, locator, timeout)
        element.click()
        logging.info(f"Clicked element: {locator}")
    except Exception as e:
        logging.error(f"Error clicking element {locator}: {e}")
        raise

def enter_text(driver, locator, text, timeout=10):
    """
    Enter text into the specified element.
    Clears any existing text before entering new text to avoid input errors.
    """
    try:
        element = wait_for_element(driver, locator, timeout)
        element.clear()
        element.send_keys(text)
        logging.info(f"Entered text into element: {locator}")
    except Exception as e:
        logging.error(f"Error entering text into element {locator}: {e}")
        raise
