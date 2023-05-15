from pages.base_page import BasePage
from pages.bikes_page import RoadBikesPage
from pages.order_tracking_page import OrderPage


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    # Lokatory strony głównej
    road_bikes_BTN = (By.CSS_SELECTOR, ".headerNav__listItem--level-1:nth-child(1) > .link .headerNav__titleTextInner")
    head_icon_BTN = (By.CSS_SELECTOR, ".headerTopBar__iconTriggerIcon--account > use")
    order_tracking_BTN = (By.CSS_SELECTOR, ".headerTopBar__accountListItem--orders .headerTopBar__accountLinkText")
    bikes_tabs = (By.CLASS_NAME, "headerNav__listItem--level-1")

class HomePage(BasePage):
#Strona główna https://canyon.com/pl-pl/
    def select_road_bikes(self):
        # Klika w 'rowery szosowe' i zwraca RoadBikesPage
        self.driver.find_element(*Locators.road_bikes_BTN).click()
        # Zwróć kolejną stronę
        return RoadBikesPage(self.driver)

    def click_tab(self, tab):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tab))
        element.click()
        return RoadBikesPage(self.driver)

    def bikes_tabs(self):
        #Znajduje wszystkie elementy z klasy z lokatora, bikes_tabs
        tabs = self.driver.find_elements(*Locators.bikes_tabs)
        #W związku z tym, że rowery są na peirwszych pięciu zakłakach, wyrzuć do listy tylko 5 pięć elementów
        bikes_tabs = tabs[:5]
        # Zwraca liste z rowerami
        return bikes_tabs


    def click_head(self):
        #Klika w łeb:
        self.driver.find_element(*Locators.head_icon_BTN).click()

    def go_to_order_page(self):
        #Klika login i zwraca strone logowania
        wait_10_sec = WebDriverWait(self.driver, 10)
        locator = Locators.order_tracking_BTN
        element = wait_10_sec.until(EC.element_to_be_clickable(locator))
        # Kliknij element
        element.click()
        return OrderPage(self.driver)


    def _verify_page(self):
        pass