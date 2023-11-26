import pytest
from pages.home_page import HomePage
from utils.config import *

@pytest.mark.homepagesearch
def test_search_home(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.search(SEARCH_QUERY) 
    home_page.wait_for_element_to_be_visible(home_page.locators.SEARCH_RETURN, 10)

@pytest.mark.homepagenquire
def test_enquire_message(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.enquiry(VALID_EMAIL, SUBJECT, MESSAGE)
    home_page.wait_for_element_to_be_visible(home_page.locators.AFTER_ENQUIRE, 10)
    