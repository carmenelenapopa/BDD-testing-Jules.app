from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class Sign_in_page(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Enter your password']")
    ERROR_MSG = (By.XPATH, '//div/p')
    LOGIN_BUTTON = (By.XPATH, "//div/button")


    def enter_email(self):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys("carmen@popa.ro")

    def enter_password(self, password):
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def clear_password(self):
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys(Keys.CONTROL + 'a')
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys(Keys.BACKSPACE)

    def error_msg_displayed(self):
        # WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.ERROR_MSG))
        # error_msg = self.chrome.find_element(*self.ERROR_MSG)
        # assert error_msg.is_displayed(), f"Error: Password error message is not displayed"
        self.chrome.find_element(*self.ERROR_MSG).is_displayed()

    def login_button_status(self):
        button_enabled = self.chrome.find_element(*self.LOGIN_BUTTON).is_enabled()
        assert button_enabled == False, f'Error! Button should be disabled'







