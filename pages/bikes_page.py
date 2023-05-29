from pages.base_page import BasePage
from pages.bikes_sorted_page import RoadBikesSortedPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    #Lokatory do testów sortowania
    product_filters_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectTrigger")
    sort_by_prices_acs_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectListItem:nth-child(1) > .productFilters__sortSelectListButton")
    sort_by_prices_desc_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectListItem:nth-child(2) > .productFilters__sortSelectListButton")

    #Lokatory do sprawdzenia poprawności obliczania ceny miesięcznej w systemie ratalnym
    show_more_items_BTN = (By.CLASS_NAME, "productGrid__viewMore")
    bikes_prices = (By.CLASS_NAME, 'productTile__priceSale')
    monthly_prices = (By.CLASS_NAME, 'productTile__priceMonthly')
    rowery = (By.CLASS_NAME, 'product-grid__items')

class RoadBikesPage(BasePage):
    """
    Strona rowery szosowe
    """
    def click_product_filters(self):
        self.driver.execute_script("window.scrollTo(0,3000)")
        element = self.driver.find_element(*Locators.product_filters_BTN)
        self.driver.execute_script("arguments[0].click();", element)
        # okno2 = self.driver.find_element(*Locators.okno_2)
        # okno2.location_once_scrolled_into_view

    def sort_by_price_acs(self):
        # Sortuje po cenie
        # self.driver.execute_script("window.scrollTo(0,5000)")
        #Sortowanie po cenie rosnąco i zwraca stronę z posortowanymi rowerami
        element = self.driver.find_element(*Locators.sort_by_prices_acs_BTN)
        self.driver.execute_script("arguments[0].click();", element)
        return RoadBikesSortedPage(self.driver)

    def sort_by_price_desc(self):
        wait = WebDriverWait(self.driver, 5)
        locator = Locators.sort_by_prices_desc_BTN
        element = wait.until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return RoadBikesSortedPage(self.driver)

    def catch_all_prices(self):
        # Znajduje wszytskie elementy z ceną, usuwa znak zł i kropke, zmienia na int i dodaje do listy
        bikes_prices = self.driver.find_elements(*Locators.bikes_prices)
        #Czeka, aż lista zostanie załadowana
        prices = []
        for i in bikes_prices:
            cena = i.text
            #zamienia "Od 58.399 ZŁ" na "58399:
            if cena.startswith("Od"):
                cena_float = float(cena.replace(" ZŁ", "").replace(".", "").replace(",",".").replace("Od ", ""))
                prices.append(cena_float)
            #Zamienia "21.959,10 ZŁ" na "21959.1"
            else:
                cena_float = float(cena.replace(" ZŁ", "").replace(".", "").replace(",","."))
                prices.append(cena_float)
        # Zwraca listę z cenami
        return prices

    def catch_monthly_prices(self):
        # Znajduje wszytskie elementy z ceną miesięczną, usuwa znak zł i kropke, zmienia na int i dodaje do listy

        monthly_bikes_prices = self.driver.find_elements(*Locators.monthly_prices)
        monthly_prices = []
        for i in monthly_bikes_prices:
            cena = i.text
            cena_int = float(cena.replace("lub od ", "").replace(".", "").replace(" ZŁ/msc", "").replace(",", "."))
            monthly_prices.append(cena_int)
        # Zwraca listę z cenami
        return monthly_prices

    def click_tab(self, tab):
        wait_5s = WebDriverWait(self.driver, 5)
        locator = tab
        element = wait_5s.until(EC.presence_of_element_located(locator))
        element.click()

    def wait_for_bikes(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-grid__items')))

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
    def go_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def click_close(self):
        pass


