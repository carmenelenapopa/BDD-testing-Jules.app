from behave import *

@given('sign_in: I am on jules sign in page')
def step_impl(context):
    context.verify_url_object.navigate_to_sign_in_page()

@when('sign_in: I click on the Sign up link')
def step_impl(context):
    context.verify_url_object.click_on_sign_up_link()

@then('sign_up: Sign up page opens')
def step_impl(context):
    context.verify_url_object.verify_sign_up_page()

@given('sign_up: I am on jules.app sign up page')
def step_impl(context):
    context.verify_url_object.navigate_to_sign_up_page()

@when('sign_up: I click on the Sign In link')
def step_impl(context):
    context.verify_url_object.click_on_sign_in_page()


@then('sign_in: Sign In page opens')
def step_impl(context):
    context.verify_url_object.verify_sign_in_page()
