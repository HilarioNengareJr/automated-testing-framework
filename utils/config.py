# For Registering User

REGISTRATION_URL = "http://127.0.0.1:5000/register"
LOGIN_URL = "http://127.0.0.1:5000/login"

VALID_USERNAME = "test user"
VALID_EMAIL = "testuser@gmail.com"
VALID_PASSWORD = "12345MyStrongPassword"

INVALID_USERNAME = " " # Is left empty therefore not valid
INVALID_EMAIL =  "testuser.com" # Does not conform to email standards
INVALID_PASSWORD = " " # Is empty therefore not valid

REGISTRATION_SUCCESS_MESSAGE = f"Registration successful! Welcome, {VALID_USERNAME}!"

