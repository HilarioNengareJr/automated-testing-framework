from pages.base_page import BasePage
from locators.register_page_locators import RegisterLocators
from utils.config import REGISTRATION_URL

class RegisterPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegisterLocators()
        
    def register(self, username, email, password):
        self.driver.find_element(*self.locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.locators.SUBMIT_INPUT).click()

    
    def register_success_message(self):
        return self.driver.find_element(*self.locators.WELCOME_MESSAGE).is_displayed()
    

    def register_error_message(self):
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).is_displayed()
    
    def open(self):
        super().open(REGISTRATION_URL) 
  