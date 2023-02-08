Feature: Check the base page functionality

  Background:
    Given base: I am on the base page

  @test1
  Scenario: I am searching for an item
    When base: I search "iPhone 14 pro max" in the search bar
    Then base: I click on the search button
    Then base: The URL has changed