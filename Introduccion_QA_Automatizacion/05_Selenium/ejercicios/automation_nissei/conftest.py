# project/conftest.py

import pytest
import logging

def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler("test_log.log"),
        logging.StreamHandler()
    ])

@pytest.fixture(scope='session')
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
