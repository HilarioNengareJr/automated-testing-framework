import pytest
import allure
from pages.login_page import LoginPage
from utils.config import *

@allure.feature("Login Page")
@allure.description("This test attempts to login with registered credentials./n/nFails if any criteria is not met.")
@allure.label("Software Engineer", "Hilario Junior Nengare")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(LOGIN_URL, name="Login Page")
@pytest.mark.login
def test_successful_login(driver):
    
    with allure.step("step 1: Entrance of credentials."):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_EMAIL, VALID_PASSWORD)
    
    with allure.step("step 2: Wait for properties page."):
        login_page.wait_for_element_to_be_visible(login_page.locators.PROPERTIES_PAGE,10)
    
    with allure.step("step 3: Test succeeds when properties page shows."):
        assert login_page.login_success_message()

"""@allure.feature("Login Page Fail")
@allure.description("This test attempts to fail to login. Makes usage of invalid credentials.")
@allure.label("Software Engineer", "Hilario Junior Nengare")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(LOGIN_URL, name="Login Page")
@pytest.mark.login_fail
def test_login_fail(driver):
    
    with allure.step("Step 1: Enter Invalid credentials. "):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
    
    with allure.step("Step 2: Properties page does not show."):
        login_page.wait_for_element_to_be_visible(login_page.locators.WELCOME_MESSAGE,20)
    
    with allure.step("Step 3: The test succeeds if authentication fails."):
        assert not login_page.login_success_message()"""