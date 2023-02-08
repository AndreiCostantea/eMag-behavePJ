from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.favourites_page import FavouritesPage

def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.cart_page = CartPage()
    context.favourites_page = FavouritesPage()
def after_all(context):
    context.browser.close()
