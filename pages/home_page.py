from utils.config import HOME_PAGE_URL
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()
    
    def search(self, search_query):
        self.driver.find_element(*self.locators.SEARCH_INPUT).send_keys(search_query)
        self.driver.find_element(*self.locators.FIND_INPUT).click()
    
    def enquiry(self, email, subject, message):
        button = self.driver.find_element(*self.locators.OPEN_MESSAGE_MODAL)
        self.driver.execute_script("arguments[0].click();", button)
        self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.locators.SUBJECT_FIELD).send_keys(subject)
        self.driver.find_element(*self.locators.MESSAGE_BOX).send_keys(message)
        self.driver.find_element(*self.locators.ENQUIRE).click()
    
    def open(self):
        super().open(HOME_PAGE_URL)