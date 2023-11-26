from selenium.webdriver.common.by import By

class HomePageLocators:
    SEARCH_INPUT = (By.NAME, 'query')
    FIND_INPUT = (By.ID, 'find-btn')
    OPEN_MESSAGE_MODAL = (By.ID, 'openMessageModal')
    EMAIL_FIELD = (By.NAME, 'email')
    SUBJECT_FIELD = (By.NAME, 'subject')
    MESSAGE_BOX = (By.ID, 'message')
    ENQUIRE = (By.ID, 'enquire')
    SEARCH_RETURN = (By.CLASS_NAME, 'property')
    AFTER_ENQUIRE = (By.CLASS_NAME, 'form-status-message')