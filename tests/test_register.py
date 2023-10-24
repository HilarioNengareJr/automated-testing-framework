import pytest
from pages.register_page import RegisterPage
from utils.config import *
from conftest import driver

@pytest.mark.register
def test_successful_register(driver):  
    register_page = RegisterPage(driver)  
    register_page.open()
    register_page.register(VALID_USERNAME, VALID_EMAIL, VALID_PASSWORD)
    register_page.go_to()
    
    assert register_page.register_success_message()

@pytest.mark.register
def test_failure_register(driver): 
    register_page = RegisterPage(driver)  
    register_page.open()
    register_page.register(VALID_EMAIL, VALID_USERNAME, VALID_PASSWORD)
    assert register_page.register_error_message()
