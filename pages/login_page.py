from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    LOGINURL = 'https://auth.emag.ro/user/login'
    CONTINUEBTN = (By.ID, 'user_login_continue')
    ERRORMSGEMAIL = (By.XPATH, '//div[contains(text(),"Câmp obligatoriu")]')
    EMAILINPUT = (By.XPATH, '//input[@id="user_login_email"]')
    PASSWORDINPUT = (By.XPATH, '//input[@id="user_login_password"]')
    ERRORMSGINVALIDEMAIL = (By.XPATH, '//div[contains(text(),"Email invalid")]')
    INTRODUPAROLAMSG = (By.XPATH, '//label[contains(text(),"Introdu parola contului tău eMAG")]')
    NEEDHELPBTN = (By.LINK_TEXT, 'Ai nevoie de ajutor?')

    def checkNewUrl(self):
        actual = self.driver.current_url
        expected = 'https://auth.emag.ro/user/login'

        assert actual == expected, 'The new URL is wrong'

    def clickContinue(self):
        self.driver.find_element(*self.CONTINUEBTN).click()
        sleep(8)

    def errorMsgDisplayed(self):
        actual = self.driver.find_element(*self.ERRORMSGEMAIL).is_displayed()
        expected = True

        assert actual == expected, 'Error message is not displayed'

    def emailInput(self, email):
        self.driver.find_element(*self.EMAILINPUT).send_keys(email)
        sleep(1.5)

    def passwordInput(self, pwd):
        self.driver.find_element(*self.PASSWORDINPUT).send_keys(pwd)
        sleep(1.5)

    def errorMsgDisplayedInvalidEmail(self):
        actual = self.driver.find_element(*self.ERRORMSGINVALIDEMAIL).is_displayed()
        expected = True

        assert actual == expected, 'Error message is not displayed'

    def introduParolaDisplayed(self):
        actual = self.driver.find_element(*self.INTRODUPAROLAMSG).is_displayed()
        expected = True
        assert actual == expected, 'Message is not displayed'

    def clickNeedHelp(self):
        self.driver.find_element(*self.NEEDHELPBTN).click()
        sleep(5)

    def checkNeedHelpURL(self):
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/help/cum-ma-loghez/'

        assert actual == expected, f'The new URL is wrong actual: {actual}'

    def checkSuccessfulLoginURL(self):
        sleep(3)
        actual = self.driver.current_url
        expected = 'https://www.emag.ro/'

        assert actual == expected, f'The new URL is wrong actual: {actual}'

    def changeTab(self):
        x = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        child = self.driver.window_handles[1]
        self.driver.switch_to.window(child)