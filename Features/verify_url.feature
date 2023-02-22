Feature: Verify sign in and login link on jules.app


  Scenario: I check if the sign up page opens when I click on sign up link
    Given sign_in: I am on jules sign in page
    When sign_in: I click on the Sign up link
    Then sign_up: Sign up page opens


  Scenario: I check if the sign in page opens when I click on sign up link
    Given sign_up: I am on jules.app sign up page
    When sign_up: I click on the Sign In link
    Then sign_in: Sign In page opens
