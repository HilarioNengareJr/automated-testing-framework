import pytest
from pages.login_page import LoginPage
from utils.config import *
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    
    WebDriverWait(driver, 30).until(
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
    
    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                login_page.locators.WELCOME_MESSAGE
                )
            )
        
    except TimeoutException:
        print('Successful Failure')
        
    assert not login_page.login_success_message()