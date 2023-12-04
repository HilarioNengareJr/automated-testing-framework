import pytest
import allure
from pages.register_page import RegisterPage
from utils.config import *

@allure.feature("Registration Page")
@allure.description("This test attempts to register using valid credentials./n/nFails if there is an error.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(REGISTRATION_URL, name="Registration Page")
@pytest.mark.register
def test_successful_register(driver): 
    
    with allure.step("Step 1: Enter valid credentials."): 
        register_page = RegisterPage(driver)  
        register_page.open()
        register_page.register(VALID_USERNAME, VALID_EMAIL, VALID_PASSWORD)
    
    with allure.step("Step 2: Wait for pop-up."):
        register_page.wait_for_element_to_be_visible(register_page.locators.WELCOME_MESSAGE, 20)
    
    with allure.step("Step 3: Test succeeds if pop-up shows."):
        assert register_page.register_success_message()
        
"""
@allure.feature("Registration Page")
@allure.description("This test attempts to fail registration using invalid credentials./n/nFails if there is an error.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(REGISTRATION_URL, name="Registration Page")
@pytest.mark.register_fail
def test_fail_register(driver):
    
    with allure.step("Step 1: Enter invalid credentials."):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.register(INVALID_USERNAME, INVALID_EMAIL, INVALID_PASSWORD)
        
    with allure.step("Step 2: Wait for pop-up"):
        register_page.wait_for_element_to_be_visible(register_page.locators.WELCOME_MESSAGE, 10)
    
    with allure.step("Step 3: Test succeeds if registration fails."):
        assert not register_page.register_success_message()
"""