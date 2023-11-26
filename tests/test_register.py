import pytest
from pages.register_page import RegisterPage
from utils.config import *

@pytest.mark.register
def test_successful_register(driver):  
    register_page = RegisterPage(driver)  
    register_page.open()
    register_page.register(VALID_USERNAME, VALID_EMAIL, VALID_PASSWORD)
    register_page.wait_for_element_to_be_visible(register_page.locators.WELCOME_MESSAGE, 20)
    assert register_page.register_success_message()

    
@pytest.mark.register_fail
def test_fail_register(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register(INVALID_USERNAME, INVALID_EMAIL, INVALID_PASSWORD)
    register_page.wait_for_element_to_be_visible(register_page.locators.WELCOME_MESSAGE, 10)
    assert not register_page.register_success_message()
