from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    show_more_items_BTN = (By.CLASS_NAME, "productGrid__viewMore")
    bikes = (By.CLASS_NAME, "productTileDefault__price")
    bikes_prices = (By.CLASS_NAME, "productTile__priceSale")
    price_original = (By.CLASS_NAME, "productTile__priceOriginal")

class RoadBikesSortedPage(BasePage):

    def show_more_items(self):
        # czekaj tyle razy na element, ile go znajdziesz
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

    def catch_all_sale_prices(self):
        # dla tej funkcji ustawione wait 0.05 -> mamy tylko czekać aż pełna lista cen rowerów będzie załadowana, jest to zdefoniowane przy bikes
        # w przeciwnym wypadku będzie czekał 10s (zdefiniowane w setupie) na każdy element z listy bikes (czyli na każdy rower w sklepie)
        self.driver.implicitly_wait(0.05)
        prices_text = []

        # Czekamy 5s na załadowanie wszystkich elementów z listy
        wait_3s = WebDriverWait(self.driver, 5)
        locator = Locators.bikes
        bikes = wait_3s.until(EC.visibility_of_all_elements_located(locator))

        # Dla każego roweru próbuje znaleźć zdefiniowaną cenę, ale jeśli posiada cenę oryginalną to właśnie ją bierzemy do porównania
        # W związku z tym najpierw próbuje znaleźć cenę oryginalną, następnie cenę sale
        for bike in bikes:
            price_element = bike.find_element(*Locators.bikes_prices)
            price = price_element
            prices_text.append(price.text)

        prices = []
        # Tutaj obrabiamy tekst przy cenie - są 2 możliwości -> albo zaczyna się ("Od
        for price in prices_text:
            # zamienia "Od 58.399 ZŁ" na float "58399":
            if price.startswith("Od"):
                cena_float = float(price.replace(" ZŁ", "").replace(".", "").replace(",", ".").replace("Od ", ""))
                prices.append(cena_float)
            # Zamienia "21.959,10 ZŁ" na float "21959.1"
            else:
                cena_float = float(price.replace(" ZŁ", "").replace(".", "").replace(",", "."))
                prices.append(cena_float)

        # Zwracamy listę z cenami float
        return prices

    def catch_all_prices(self):

        #dla tej funkcji ustawione wait 0.05 -> mamy tylko czekać aż pełna lista cen rowerów będzie załadowana, jest to zdefoniowane przy bikes
        #w przeciwnym wypadku będzie czekał 10s (zdefiniowane w setupie) na każdy element z listy bikes (czyli na każdy rower w sklepie)
        self.driver.implicitly_wait(0.05)
        prices_text = []

        #Czekamy 5s na załadowanie wszystkich elementów z listy
        wait_3s = WebDriverWait(self.driver, 5)
        locator = Locators.bikes
        bikes = wait_3s.until(EC.visibility_of_all_elements_located(locator))

        #Dla każego roweru próbuje znaleźć zdefiniowaną cenę, ale jeśli posiada cenę oryginalną to właśnie ją bierzemy do porównania
        #W związku z tym najpierw próbuje znaleźć cenę oryginalną, następnie cenę sale
        for bike in bikes:
            try:
                price_element = bike.find_element(*Locators.price_original)
                price = price_element
                prices_text.append(price.text)
            except:
                price_element = bike.find_element(*Locators.bikes_prices)
                price = price_element
                prices_text.append(price.text)

        prices = []
        #Tutaj obrabiamy tekst przy cenie - są 2 możliwości -> albo zaczyna się ("Od
        for price in prices_text:
            #zamienia "Od 58.399 ZŁ" na float "58399":
            if price.startswith("Od"):
                cena_float = float(price.replace(" ZŁ", "").replace(".", "").replace(",", ".").replace("Od ", ""))
                prices.append(cena_float)
            #Zamienia "21.959,10 ZŁ" na float "21959.1"
            else:
                cena_float = float(price.replace(" ZŁ", "").replace(".", "").replace(",", "."))
                prices.append(cena_float)

        #Zwracamy listę z cenami float
        return prices

    def go_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
