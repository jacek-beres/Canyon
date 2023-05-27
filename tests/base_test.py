from pages.home_page import HomePage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.canyon.com/")
        self.driver.implicitly_wait(10)

        # Utwórz instancę BasePage
        self.base_page_object = BasePage(self.driver)
        self.base_page_object.choose_country()
        self.base_page_object.accept_cookies()


        # Utwórz instancję HomePage
        self.home_page_object = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()