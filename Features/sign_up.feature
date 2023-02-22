Feature: Jules.app sign-up test
  Background:
    Given sign_in: I am a user on jules sign in page

    Scenario: I create an account
      When sign_in: I click sign up button
      When sign_up: I click Personal radio button
      When sign_up: I click Continue button
      When sign_up: I type First name "Adela"
      When sign_up: I click Continue first name button
      When sign_up: I type Last name "Alexa"
      When sign_up: I click Continue Last name button
      When sign_up: I set my email to "abcd"
      Then sign_up: I receive message "Please enter a valid email address."











