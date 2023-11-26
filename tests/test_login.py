import pytest
from pages.login_page import LoginPage
from utils.config import *

@pytest.mark.login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    login_page.wait_for_element_to_be_visible(login_page.locators.WELCOME_MESSAGE,10)
    assert login_page.login_success_message()

@pytest.mark.login_fail
def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
    login_page.wait_for_element_to_be_visible(login_page.locators.WELCOME_MESSAGE,10)
    assert not login_page.login_success_message()