import pytest
import allure
from pages.home_page import HomePage
from utils.config import *

@allure.feature("Home Page Search Bar")
@allure.description("This search attempts to query property data./n/nThe output is a list of properties accorded to the query.")
@allure.label("Software Engineer", "Hilario Junior Nengare")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(HOME_PAGE_URL, name="Home Page searchbar")
@pytest.mark.homepagesearch
def test_search_home(driver):
    
    with allure.step("Step 1: Entering the query."):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search(SEARCH_QUERY) 
    
    with allure.step("Step 2: Verifying the output."):
        home_page.wait_for_element_to_be_visible(home_page.locators.SEARCH_RETURN, 20)
    
@allure.feature("Home Page Enquiry Form")
@allure.description("This search attempts to send an enquiry with simulated User Feedback./n/nOutput is a success message.")
@allure.label("Software Engineer", "Hilario Junior Nengare")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(HOME_PAGE_URL, name="Home Page Enquiry")
@pytest.mark.homepagenquire
def test_enquire_message(driver):
    
    with allure.step("Step 1: Opening modal for entry."):
        home_page = HomePage(driver)
        home_page.open()
        home_page.enquiry(VALID_EMAIL, SUBJECT, MESSAGE)
    
    with allure.step("Step 2: Returning a successful result."):
        home_page.wait_for_element_to_be_visible(home_page.locators.AFTER_ENQUIRE, 20)
    