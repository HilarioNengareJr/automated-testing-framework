from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_INPUT = (By.ID, "login")
    WELCOME_MESSAGE = (By.ID, "flash-popup")
    ERROR_MESSAGE = ""