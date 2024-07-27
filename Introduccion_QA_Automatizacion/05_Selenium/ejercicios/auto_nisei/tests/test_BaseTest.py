#path: Python_Selenium/Selenium_Locators_Homework/Tests/test_BaseTest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.mark.usefixtures("setup")
class BaseTest:
    @pytest.fixture(scope="session")
    def setup(self, request):
        """Setup method to initialize WebDriver before test suite execution."""
        if not hasattr(BaseTest, "driver"):
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            service = ChromeService(ChromeDriverManager().install())
            BaseTest.driver = webdriver.Chrome(service=service, options=options)
            request.addfinalizer(BaseTest.driver.quit)
        
        self.driver = BaseTest.driver
        self.driver.delete_all_cookies()  # Clean up cookies to ensure test isolation
        return self.driver

    @staticmethod
    def teardown():
        """Teardown method to close WebDriver after all tests are executed."""
        if hasattr(BaseTest, "driver"):
            BaseTest.driver.quit()

    def accept_alert(self):
        """
        Accepts a currently displayed alert.
        """
        Alert(self.driver).accept()

    def dismiss_alert(self):
        """
        Dismisses a currently displayed alert.
        """
        Alert(self.driver).dismiss()