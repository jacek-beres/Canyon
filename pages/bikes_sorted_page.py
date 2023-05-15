from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    show_more_items_BTN = (By.CSS_SELECTOR, ".js-showMoreGrid")
    bikes_prices = (By.CLASS_NAME, 'productTile__priceSale')

class RoadBikesSortedPage(BasePage):

    def show_more_items(self):
        #czekaj tyle razy na element, ile go znajdziesz
        while True:
            try:
                # Czekaj max 5s, aż element będzie klikalny
                self.driver.execute_script("window.scrollBy(0,3000)")
                wait_10_sec = WebDriverWait(self.driver, 10)
                locator = Locators.show_more_items_BTN
                element = wait_10_sec.until(EC.element_to_be_clickable(locator))
                # Kliknij element
                element.click()
            except:
                break

    def catch_all_prices(self):
        # Znajduje wszytskie elementy z ceną, usuwa znak zł i kropke, zmienia na int i dodaje do listy
        bikes_prices = self.driver.find_elements(*Locators.bikes_prices)
        prices = []
        for i in bikes_prices:
            cena = i.text
            cena_int = float(cena.replace(" ZŁ", "").replace(".", ""))
            prices.append(cena_int)
        # Zwraca listę z cenami
        return prices
