import pytest
from selenium import webdriver
from utils.config import REGISTRATION_URL

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def return_url():
    return REGISTRATION_URL
        