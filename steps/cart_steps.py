from behave import *

@when('cart: I click on the "Intoarce-te la magazin" button')
def step_impl(context):
    context.cart_page.intoarceMagazinClick()

@when('cart: I close the notification')
def step_impl(context):
    context.cart_page.exitNotification()

@when('cart: I click on "Sterge" button')
def step_impl(context):
    context.cart_page.deleteItem()

@when('cart: I click on "Muta in favorite" button')
def step_impl(context):
    context.cart_page.moveFavouriteClick()

@then('cart: The URL has changed')
def step_impl(context):
    context.cart_page.checkUrl()

@then('cart: "Cosul tau este gol" message is displayed')
def step_impl(context):
    context.cart_page.cartEmptyMsgDisplayed()

@then('cart: I am back on the base page')
def step_impl(context):
    context.cart_page.checkBaseUrl()

@then('cart: "Produsul a fost adaugat in cos" message is displayed')
def step_impl(context):
    context.cart_page.itemAddedMsgDisplayed()

@then('cart: "Cosul meu" message is displayed')
def step_impl(context):
    context.cart_page.myCartMsgDisplayed()

@then('cart: Prices are displayed')
def step_impl(context):
    context.cart_page.pricesDisplayed()

