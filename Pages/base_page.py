from Browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):
    def wait_and_click_element(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(*selector))

    def page_sign_in_url(self):
        self.chrome.get("https://jules.app/sign-in")

    def page_sign_up_url(self):
        self.chrome.get("https://jules.app/sign-up")

    def verify_url(self, expected_url):
        actual_url = self.chrome.current_url
        assert actual_url == expected_url
