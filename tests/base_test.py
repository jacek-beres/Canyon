from pages.home_page import HomePage
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver

class Locators:
    PL_BTN = (By.XPATH, '//a[@data-country="PL"]')
    accept_cookies = (By.ID, 'js-data-privacy-save-button')
class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.canyon.com/")

        self.driver.find_element(*Locators.PL_BTN).click()
        self.driver.find_element(*Locators.accept_cookies).click()

        # Utwórz instancję HomePage
        self.home_page_object = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()