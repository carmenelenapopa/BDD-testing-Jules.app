from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Sign_up_page(BasePage):
    SIGN_UP = (By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[4]/a")
    PERSONAL_BUTTON = (By.XPATH, "//input[@value='personal']")
    CONTINUE_BUTTON = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[5]/button")
    INPUT = (By.XPATH, "//input[@type='text']")
    INPUT2 = (By.XPATH, "//input[@type='text']")
    FIRST_NAME_CONTINUE_BUTTON = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[3]/button")
    LAST_NAME_CONTINUE_BUTTON = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[3]/button")
    EMAIL_CONTINUE_BUTTON = (By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[3]/button")



    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def navigate_to_sign_up_page(self):
        self.chrome.find_element(*self.SIGN_UP).click()

    def click_personal_button(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()

    def click_continue_button(self):
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def send_first_name(self, name):
        self.chrome.find_element(*self.INPUT).send_keys(name)

    def click_continue_first_name_button(self):
        self.chrome.find_element(*self.FIRST_NAME_CONTINUE_BUTTON).click()

    def send_last_name(self, name):
        self.chrome.find_element(*self.INPUT2).send_keys('Alexa')

    def click_continue_last_name_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BUTTON).click()

    def send_email(self, email):
        self.chrome.find_element(*self.INPUT).send_keys(email)

    def check_error_message_email(self):
        expected = "Please enter a valid email address."
        actual = self.chrome.find_element(By.XPATH, "/html/body/div/div/div[4]/div[2]/div/div[2]/div/p").text
        assert expected == actual
