Feature: I am an user trying to log in

  Background:
    Given base: I am on the base page
    When base: I click the "Contul meu" button

  @test20
  Scenario: I click the "Contul meu" button
    Then login: The new URL is "https://auth.emag.ro/user/login"

  @test21
  Scenario: I click "Continua" without an email input
    When login: I click "Continua" button
    Then login: Error message is displayed with message: "Camp obligatoriu"

  @test22
  Scenario: I click "Continua" with an invalid email input
    When login: I fill the email field with value: "andreicostantea"
    When login: I click "Continua" button
    Then login: Error message is displayed with message: "Email invalid"
    # => tests will not work if you dont manually get past the anti bot system
    # => there are longer sleep() functions for you to have enough time to resolve the anti bot system

  @test23
  Scenario: I click "Continua" with a valid email input
    When login: I fill the email field with value: "andrei.costantea@yahoo.com"
    When login: I click "Continua" button
    Then login: "Introdu parola contului tau eMAG" message is displayed
   # => tests will not work if you dont manually get past the anti bot system
   # => there are longer sleep() functions for you to have enough time to resolve the anti bot system

  @test24
  Scenario: I am an user who needs help with his account
    When login: I click on "Ai nevoie de ajutor?"
    Then login: A new browser tab opens, I click it
    Then login: The URL of the new tab is: "https://www.emag.ro/help/cum-ma-loghez/"

  @test25
  Scenario: I am an user connecting with correct values
    When login: I fill the email field with value: "muhahamuhaha110@yahoo.com"
    When login: I click "Continua" button
    When login: I fill the password field with value: "Parolasigura1"
    When login: I click "Continua" button
    Then login: The URL changes to: "https://www.emag.ro/"
    # => tests will not work if you dont manually get past the anti bot system
    # => there are longer sleep() functions for you to have enough time to resolve the anti bot system