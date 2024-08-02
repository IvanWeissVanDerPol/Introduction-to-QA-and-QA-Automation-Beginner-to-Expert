# project/tests/base_test.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
import logging

@pytest.mark.usefixtures("setup")
class BaseTest:
    homepage: HomePage
    driver: webdriver.Chrome
    
    @pytest.fixture(scope="class")
    def setup(self, request):
        """
        Setup method to initialize WebDriver before test execution.
        """
        logging.info("Setting up WebDriver")
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')

        # Specify the path to chromedriver.exe
        chromedriver_path = "chromedriver.exe"
        service = ChromeService(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        homepage = HomePage(driver)  # Navigate to the homepage and get the HomePage object

        request.cls.driver = driver  # This will now work
        request.cls.homepage = homepage  # Make homepage accessible in methods

        yield driver  # Ensure the teardown code runs after the test
        logging.info("Tearing down WebDriver")
        driver.quit()

    @staticmethod
    def teardown():
        """
        Teardown method to close WebDriver after all tests are executed.
        """
        if hasattr(BaseTest, "driver"):
            BaseTest.driver.quit()
