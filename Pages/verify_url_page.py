from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class Verify_url(BasePage):
    SIGN_UP = (By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[4]/a")
    LOG_IN = (By.XPATH, "//button[@data-test-id='go-to-login-btn']")


    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-inv")

    def click_on_sign_up_link(self):
        self.chrome.find_element(*self.SIGN_UP).click()

    def verify_sign_up_page(self):
        self.chrome.current_url

    def navigate_to_sign_up_page(self):
        self.chrome.get("https://jules.app/sign-up")

    def click_on_sign_in_page(self):
        self.chrome.find_element(*self.LOG_IN).click()

    def verify_sign_in_page(self):
        self.chrome.current_url




