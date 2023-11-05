import pytest
from pages.login_page import LoginPage
from utils.config import *
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            login_page.locators.WELCOME_MESSAGE
        )
    )
    
    assert login_page.login_success_message()

@pytest.mark.login_fail
def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(INVALID_EMAIL, INVALID_PASSWORD)