from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Locators:
    email_field = (By.ID, "dwfrm_ordertracking_email")
    order_nr_field = (By.ID, "dwfrm_ordertracking_orderNo")
    email_alert = (By.CSS_SELECTOR, ".inputText:nth-child(1) > .inputText__error")
    order_nr_alert = (By.CSS_SELECTOR, ".inputText:nth-child(2) > .inputText__error")
    confirm_BTN = (By.ID, 'js-order-tracking-save')

class OrderPage(BasePage):
    "Strona logowania"
    def enter_email(self, email):
        self.driver.find_element(*Locators.email_field).send_keys(email)

    def enter_order_nr(self, orderNr):
        self.driver.find_element(*Locators.order_nr_field).send_keys(orderNr)


    def click_next(self):
        self.driver.find_element(*Locators.confirm_BTN).click()

    def catch_email_message(self):
        try:
            locator = Locators.email_alert
            wait_2s = WebDriverWait(self.driver, 2)
            wait_2s.until(EC.visibility_of_element_located(locator))
            email_alert = self.driver.find_element(*Locators.email_alert)
            return email_alert

        except:
            email_alert = None
            return email_alert

    def catch_order_nr_message(self):
        try:
            locator = Locators.order_nr_alert
            wait_2s = WebDriverWait(self.driver, 2)
            wait_2s.until(EC.visibility_of_element_located(locator))
            order_nr_alert = self.driver.find_element(*Locators.order_nr_alert)
            return order_nr_alert

        except:
            order_nr_alert = None
            return order_nr_alert


    def login(self, email):
        pass


