Feature: Check the favourites page functionality

  Background:
    Given base: I am on the base page

  @test40
  Scenario: I click on the heart symbol and verify if the URL has changed
    When base: I click on the heart symbol
    Then favourites: The URL has changed

  @test41
  Scenario: I go to favourites without adding any item
    When base: I click on the heart symbol
    Then favourites: "0 produse" message is displayed

  @test42
  Scenario: I add an item to favourites
    When base: I search "smartwatch" in the search bar
    Then base: I click on the search button
    When base: I add the first item to favourites
    When base: I click on the heart symbol
    Then favourites: Favourite message is displayed

  @test43
  Scenario: I go to favourites and click "Vezi produse" button
    When base: I click on the heart symbol
    When favourites: I click on "Vezi produse" button
    Then favourites: Check new URL

