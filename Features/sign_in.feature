Feature: Jules.app sign-in test without entering password
  Background:
    Given sign_in: I am a user on jules sign in page

    Scenario: I check if the user can log in without entering a password
      When sign_in: I enter a correct email address in Email field "carmen@carmen.ro"
      When sign_in: I leave Password field empty
      Then sign_in: I verify if the error ‘Please enter your password!’ is displayed
      Then sign_in: I verify if my Log in Button is disabled

