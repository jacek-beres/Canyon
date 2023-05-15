from pages.base_page import BasePage
from pages.bikes_sorted_page import RoadBikesSortedPage
from pages.bikes_filtered_page import BikesFilteredPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Locators:
    #Lokatory do testów sortowania
    product_filters_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectTrigger")
    sort_by_prices_acs_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectListItem:nth-child(1) > .productFilters__sortSelectListButton")
    sort_by_prices_desc_BTN = (By.CSS_SELECTOR, ".productFilters__sortSelectListItem:nth-child(2) > .productFilters__sortSelectListButton")

    #Lokatory do sprawdzenia poprawności obliczania ceny miesięcznej w systemie ratalnym
    show_more_items_BTN = (By.CSS_SELECTOR, ".js-showMoreGrid")
    bikes_prices = (By.CLASS_NAME, 'productTile__priceSale')
    monthly_prices = (By.CLASS_NAME, 'productTile__priceMonthly')

    logo_BTN = (By.CSS_SELECTOR, ".headerTopBar__logo use")



    #Lokatory do testów filtrowania
    show_filters_BTN = (By.CSS_SELECTOR, ".productFilters__buttonText--open")
    family_filter_BTN = (By.CSS_SELECTOR, ".productFilterGroup:nth-child(4) .productFilterGroup__headingName")
    family_1_BTN = (By.CSS_SELECTOR, ".productFilterGroup:nth-child(4) .productFilterGroup__listItem:nth-child(1) .icon")

class RoadBikesPage(BasePage):
    """
    Strona rowery szosowe
    """
    def click_product_filters(self):
        # actions = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0,3000)")
        self.driver.find_element(*Locators.product_filters_BTN).click()
        # okno2 = self.driver.find_element(*Locators.okno_2)
        # okno2.location_once_scrolled_into_view

    def sort_by_price_acs(self):
        # Sortuje po cenie

        self.driver.execute_script("window.scrollTo(0,5000)")
        #Sortowanie po cenie rosnąco i zwraca stronę z posortowanymi rowerami
        self.driver.find_element(*Locators.sort_by_prices_acs_BTN).click()
        return RoadBikesSortedPage(self.driver)
        #Klika w panel filtrów

    def sort_by_price_desc(self):
        self.driver.execute_script("window.scrollTo(0,5000)")
        #Sortowanie po cenie malejąco i zwraca stronę z posortowanymi rowerami
        self.driver.find_element(*Locators.sort_by_prices_desc_BTN).click()
        return RoadBikesSortedPage(self.driver)
        #Klika w panel filtrów

    def show_filters(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(*Locators.show_filters_BTN).click()

    def expand_family(self):
        self.driver.find_element(*Locators.family_filter_BTN).click()

    def click_family(self):
        self.driver.find_element(*Locators.family_1_BTN).click()
        return BikesFilteredPage(self.driver)

    def catch_family_name(self):
        family_name = set(self.driver.find_element(*Locators.family_1_BTN).text)
        return family_name

    def catch_all_prices(self):
        # Znajduje wszytskie elementy z ceną, usuwa znak zł i kropke, zmienia na int i dodaje do listy
        bikes_prices = self.driver.find_elements(*Locators.bikes_prices)
        prices = []
        for i in bikes_prices:
            cena = i.text
            cena_int = float(cena.replace(" ZŁ", "").replace(".", "").replace(",","."))
            prices.append(cena_int)
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

    def return_home_page(self):

        self.driver.find_element(*Locators.logo_BTN).click()


    def click_close(self):
        pass


