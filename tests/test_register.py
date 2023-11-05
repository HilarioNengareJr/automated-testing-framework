import pytest
from pages.register_page import RegisterPage
from utils.config import *
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.register
def test_successful_register(driver):  
    register_page = RegisterPage(driver)  
    register_page.open()
    register_page.register(VALID_USERNAME, VALID_EMAIL, VALID_PASSWORD)
    
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            register_page.locators.WELCOME_MESSAGE
            )
    )
    
    assert register_page.register_success_message()

    
@pytest.mark.register_fail
def test_fail_register(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register(INVALID_USERNAME, INVALID_EMAIL, INVALID_PASSWORD)
    
    try:
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            register_page.locators.WELCOME_MESSAGE
            )
        )
    except Exception as e:
        print(f"successful fail {e}")
    
