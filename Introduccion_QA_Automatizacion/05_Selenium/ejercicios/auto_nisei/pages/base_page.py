from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_base_url(self, url):
        self.driver.get(url)
    def get_page_title(self):
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(text)

    def submit_form(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.submit()

    def close_onesignal_popup(self):
        try:
            # Wait for the pop-up to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "onesignal-slidedown-container"))
            )
            # Click the "No, gracias" button
            no_gracias_button = self.driver.find_element(By.ID, "onesignal-slidedown-cancel-button")
            no_gracias_button.click()
        except Exception as e:
            print("Pop-up did not appear or could not be closed:", e)