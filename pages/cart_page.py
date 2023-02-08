from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class CartPage(BasePage):
    CARTEMPTYMSG = (By.XPATH, '//div[@class="title"]')
    INTOARCEMAGAZINBTN = (By.XPATH, '//a[normalize-space()="Intoarce-te in magazin"]')
    ITEMADDEDMSG = (By.XPATH, '//h4[normalize-space()="Produsul a fost adaugat in cos"]')
    CLOSENOTIFICATIONBTN = (By.XPATH, '//button[@aria-label="Inchide"]')
    COSULMEUMSG = (By.XPATH, '//h1[normalize-space()="Cosul meu"]')
    PRODUSELIVRATEMSG = (By.XPATH, '//h2[normalize-space()="Produse livrate de Ambia Store"]')
    PRICES = (By.XPATH, '//div[@class="cart-vendor-summary"]')
    DELETEITEM = (By.LINK_TEXT, 'Sterge')
    FAVOURITEBTN = (By.LINK_TEXT, 'Muta in Favorite')

    def checkUrl(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/cart/products?ref=cart'

        assert expected == actual, 'The URL is wrong'

    def cartEmptyMsgDisplayed(self):
        actual = self.driver.find_element(*self.CARTEMPTYMSG).is_displayed()
        expected = True

        assert expected == actual, 'Message is not displayed'

    def intoarceMagazinClick(self):
        self.driver.find_element(*self.INTOARCEMAGAZINBTN).click()
        sleep(1)

    def checkBaseUrl(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/?ref=emptycart_back_to_hp_btn'

        assert expected == actual, 'The URL has not changed'

    def itemAddedMsgDisplayed(self):
        actual = self.driver.find_element(*self.ITEMADDEDMSG).is_displayed()
        expected = True

        assert expected == actual, 'Message is not displayed'

    def exitNotification(self):
        self.driver.find_element(*self.CLOSENOTIFICATIONBTN).click()
        sleep(0.5)

    def myCartMsgDisplayed(self):
        actual = self.driver.find_element(*self.COSULMEUMSG).is_displayed()
        expected = True

        assert expected == actual, 'Message is not displayed'

    def pricesDisplayed(self):
        actual = self.driver.find_element(*self.PRICES).is_displayed()
        expected = True

        assert expected == actual, 'Prices are not displayed'

    def deleteItem(self):
        self.driver.find_element(*self.DELETEITEM).click()
        sleep(1)

    def moveFavouriteClick(self):
        self.driver.find_element(*self.FAVOURITEBTN).click()
        sleep(2.5)