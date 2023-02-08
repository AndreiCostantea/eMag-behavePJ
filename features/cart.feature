Feature: Check the cart page functionality

  Background:
    Given base: I am on the base page

  @test30
  Scenario: I click on the cart icon and verify if the URL has changed
    When base: I click on the cart icon button
    Then cart: The URL has changed

  @test31
  Scenario: I click on the cart icon without adding an item to the cart
    When base: I click on the cart icon button
    Then cart: "Cosul tau este gol" message is displayed

  @test32
  Scenario: I click on the cart icon without adding an item to the cart then I click "Intoarce-te in magazin" button
    When base: I click on the cart icon button
    When cart: I click on the "Intoarce-te la magazin" button
    Then cart: I am back on the base page

  @test33
  Scenario: I add an item to my shopping cart
    When base: I add an item to the cart
    Then cart: "Produsul a fost adaugat in cos" message is displayed

  @test34
  Scenario: I go to my shopping cart with the item in it
    When base: I add an item to the cart
    When cart: I close the notification
    When base: I click on the cart icon button
    Then cart: "Cosul meu" message is displayed
    Then cart: Prices are displayed

  @test35
  Scenario: I delete the item from my shopping cart
    When base: I add an item to the cart
    When cart: I close the notification
    When base: I click on the cart icon button
    When cart: I click on "Sterge" button
    Then cart: "Cosul tau este gol" message is displayed

  @test36
  Scenario: I add the item from cart to favourites
    When base: I add an item to the cart
    When cart: I close the notification
    When base: I click on the cart icon button
    When cart: I click on "Muta in favorite" button
    Then cart: "Cosul tau este gol" message is displayed
