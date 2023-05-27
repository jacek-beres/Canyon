from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class Locators:
    PL_BTN = (By.XPATH, '//a[@data-country="PL"]')
    accept_cookies = (By.ID, 'js-data-privacy-save-button')
class BasePage:
    """
    Klasa bazowa każdej strony.
    Nie będzie miała instancji. Faktyczne strony będą
    po niej dziedziczyć
    """
    def __init__(self, driver):
        self.driver = driver
        # Każda strona będzie się automatycznie sprawdzała
        self._verify_page()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def choose_country(self):
        self.driver.find_element(*Locators.PL_BTN).click()

    def accept_cookies(self):
        self.driver.find_element(*Locators.accept_cookies).click()

    def _verify_page(self):
        """
        Weryfikacja strony
        """
        pass