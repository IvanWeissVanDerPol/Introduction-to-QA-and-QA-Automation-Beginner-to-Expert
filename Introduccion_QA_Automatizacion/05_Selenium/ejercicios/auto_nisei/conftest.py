import pytest
from selenium import webdriver
import chromedriver_py

from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = chromedriver_py.binary_path
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def config():
    return {
        "credentials": {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        },
        "google_credentials": {
            "email": "fakemailpoli@gmail.com",
            "password": "FakeMail123!"
        },
        "base_url": "https://nissei.com/py/"
    }
