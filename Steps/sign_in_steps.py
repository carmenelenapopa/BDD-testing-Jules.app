from behave import *
import time

from selenium.webdriver.support.wait import WebDriverWait


@when('sign_in: I enter a correct email address in Email field "carmen@carmen.ro"')
def step_impl(context):
    time.sleep(5)
    context.sign_in_object.enter_email()


@when('sign_in: I leave Password field empty')
def step_impl(context):
    time.sleep(5)
    context.sign_in_object.enter_password("pswd")
    time.sleep(5)
    context.sign_in_object.clear_password()
    time.sleep(5)

@then('sign_in: I verify if the error ‘Please enter your password!’ is displayed')
def step_impl(context):
    time.sleep(3)
    context.sign_in_object.error_msg_displayed()


@then('sign_in: I verify if my Log in Button is disabled')
def step_impl(context):
    time.sleep(3)
    context.sign_in_object.login_button_status()
