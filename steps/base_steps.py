from behave import *

@given('base: I am on the base page')
def step_impl(context):
    context.base_page.goto_base_page()

@when('base: I click the "Contul meu" button')
def step_impl(context):
    context.base_page.clickContulMeu()

@when('base: I click on the cart icon button')
def step_impl(context):
    context.base_page.clickCosulMeu()

@when('base: I add an item to the cart')
def step_impl(context):
    context.base_page.addItem()

@when('base: I click on the heart symbol')
def step_impl(context):
    context.base_page.clickFavourites()

@when('base: I search "{item}" in the search bar')
def step_impl(context, item):
    context.base_page.searchItem(item)

@when('base: I add the first item to favourites')
def step_impl(context):
    context.base_page.addToFavourite()

@then('base: I click on the search button')
def step_impl(context):
    context.base_page.searchClick()

@then('base: The URL has changed')
def step_impl(context):
    context.base_page.checkNewURL()