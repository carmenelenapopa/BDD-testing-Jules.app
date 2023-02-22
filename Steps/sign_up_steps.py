import time

from behave import *

@given('sign_in: I am a user on jules sign in page')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.navigate_to_sign_in_page()


@when('sign_in: I click sign up button')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.navigate_to_sign_up_page()


@when('sign_up: I click Personal radio button')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.click_personal_button()


@when('sign_up: I click Continue button')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.click_continue_button()


@when('sign_up: I type First name "Adela"')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.send_first_name('Adela')


@when('sign_up: I click Continue first name button')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.click_continue_first_name_button()


@when('sign_up: I type Last name "Alexa"')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.send_last_name('Alexa')


@when('sign_up: I click Continue Last name button')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.click_continue_last_name_button()


@when('sign_up: I set my email to "abcd"')
def step_impl(context):
    time.sleep(5)
    context.sign_up_object.send_email('abcd')


@then('sign_up: I receive message "Please enter a valid email address."')
def step_impl(context):
    context.sign_up_object.check_error_message_email()

