from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class FavouritesPage(BasePage):
    FAVMESSAGE = (By.XPATH, '//h3[normalize-space()="Favorite"]')
    ZEROITEMSMSG = (By.XPATH, '//span[@class="products-number hidden-xs js-products-count"]')
    VEZIPRODUSEBUTTON = (By.XPATH, '//a[normalize-space()="Vezi produse"]')

    def checkUrl(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/favorites?ref=ua_favorites'

        assert expected == actual, 'The URL is wrong'

    def favMessageDisplayed(self):
        actual = self.driver.find_element(*self.FAVMESSAGE).is_displayed()
        expected = True

        assert expected == actual, 'Message is not displayed'

    def zeroItemsMsg(self):
        actual = self.driver.find_element(*self.ZEROITEMSMSG).text
        expected = "0 produse"

        assert expected == actual, 'Message is wrong'

    def clickVeziProd(self):
        self.driver.find_element(*self.VEZIPRODUSEBUTTON).click()
        sleep(1)

    def checkNewURL(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/homepage?ref=fav_anonymous_empty-list_btn'

        assert expected == actual, 'The URL did not change'