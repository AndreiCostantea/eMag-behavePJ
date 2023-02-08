from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep

class BasePage(Browser):
    CONTULMEUBUTTON = (By.CSS_SELECTOR, '.em.em-user2.navbar-icon')
    COSULMEUBUTTON = (By.CSS_SELECTOR, '.em.em-cart2.navbar-icon')
    FAVOURITESBUTTON = (By.CSS_SELECTOR, '.em.em-heart.navbar-icon')
    ITEM = (By.XPATH, '//button[@data-pnk="DZDZXTMBM"]//i[@class="em em-cart_fill "]')
    SEARCHBAR = (By.XPATH, '//input[@id="searchboxTrigger"]')
    SEARCHBUTTON = (By.XPATH, '//button[@class="btn btn-default searchbox-submit-button"]')

    def goto_base_page(self):
        self.driver.get('https://www.emag.ro/')
        sleep(1)

    def clickContulMeu(self):
        self.driver.find_element(*self.CONTULMEUBUTTON).click()
        sleep(1)

    def clickCosulMeu(self):
        self.driver.find_element(*self.COSULMEUBUTTON).click()
        sleep(1)

    def clickFavourites(self):
        self.driver.find_element(*self.FAVOURITESBUTTON).click()
        sleep(1)

    def addItem(self):
        self.driver.execute_script('window.scrollTo(0, 650)')
        sleep(1.5)
        self.driver.find_element(*self.ITEM).click()
        sleep(1)

    def searchItem(self, item):
        self.driver.find_element(*self.SEARCHBAR).send_keys(item)
        sleep(1.5)

    def searchClick(self):
        self.driver.find_element(*self.SEARCHBUTTON).click()
        sleep(1)

    def addToFavourite(self):
        self.driver.find_element(By.XPATH, '//body[1]/div[3]/div[2]/div[1]/section[1]/div[1]/div[3]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/button[1]/i[1]').click()
        sleep(2)

    def checkNewURL(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/'

        assert expected != actual, 'The URL did not change'