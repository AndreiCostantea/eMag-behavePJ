from behave import *

@when('favourites: I click on "Vezi produse" button')
def step_impl(context):
    context.favourites_page.clickVeziProd()

@then('favourites: The URL has changed')
def step_impl(context):
    context.favourites_page.checkUrl()

@then('favourites: Favourite message is displayed')
def step_impl(context):
    context.favourites_page.favMessageDisplayed()

@then('favourites: "0 produse" message is displayed')
def step_impl(context):
    context.favourites_page.zeroItemsMsg()

@then('favourites: Check new URL')
def step_impl(context):
    context.favourites_page.checkNewURL()