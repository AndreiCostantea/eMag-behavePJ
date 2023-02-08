from behave import *

@when('login: I click "Continua" button')
def step_impl(context):
    context.login_page.clickContinue()

@when('login: I fill the email field with value: "{email}"')
def step_impl(context, email):
    context.login_page.emailInput(email)

@when('login: I fill the password field with value: "{pwd}"')
def step_impl(context, pwd):
    context.login_page.passwordInput(pwd)

@when('login: I click on "Ai nevoie de ajutor?"')
def step_impl(context):
    context.login_page.clickNeedHelp()

@then('login: The new URL is "https://auth.emag.ro/user/login"')
def step_impl(context):
    context.login_page.checkNewUrl()

@then('login: Error message is displayed with message: "Camp obligatoriu"')
def step_impl(context):
    context.login_page.errorMsgDisplayed()

@then('login: Error message is displayed with message: "Email invalid"')
def step_impl(context):
    context.login_page.errorMsgDisplayedInvalidEmail()

@then('login: "Introdu parola contului tau eMAG" message is displayed')
def step_impl(context):
    context.login_page.introduParolaDisplayed()

@then('login: The URL of the new tab is: "https://www.emag.ro/help/cum-ma-loghez/"')
def step_impl(context):
    context.login_page.checkNeedHelpURL()

@then('login: The URL changes to: "https://www.emag.ro/"')
def step_impl(context):
    context.login_page.checkSuccessfulLoginURL()

@then('login: A new browser tab opens, I click it')
def step_impl(context):
    context.login_page.changeTab()
