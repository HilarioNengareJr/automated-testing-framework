from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators
from utils.config import LOGIN_URL

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()
            
    def login(self, email, password):
        self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.locators.SUBMIT_INPUT).click()
    
    def login_success_message(self):
        return self.driver.find_element(*self.locators.PROPERTIES_PAGE).is_displayed()
    
    def open(self):
        super().open(LOGIN_URL)
    