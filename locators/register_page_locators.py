from selenium.webdriver.common.by import By

class RegisterLocators:
    USERNAME_INPUT = (By.ID, 'username')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_INPUT = (By.ID, 'sign-up')
    WELCOME_MESSAGE = (By.ID, 'flash-popup')
    ERROR_MESSAGE = (By.ID, 'flash-popup')