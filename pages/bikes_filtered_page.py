from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    show_more_items_BTN = (By.CSS_SELECTOR, ".js-showMoreGrid")
    names = (By.CLASS_NAME, 'productTileDefault__productNameWrapper')
    selected = (By.CLASS_NAME, 'productFilterGroup__listItem')

class BikesFilteredPage(BasePage):

    #Znajdź wszystkie nazwy rowerów
    def catch_model_names(self):

        bikes_names = self.driver.find_elements(*Locators.names)
        names = []
        #Zostawienie tylko pierwszego słowa w nazwie roweru (powinno odpowiadać zaznaczonej rodzinie)
        for i in bikes_names:
            name = i.text
            name_first_word = name.split()[0]
            names.append(name_first_word)

        #Zamiana listy na zbiór
        names = set(names)

        return names

    #Znajdz wszystkie zaznaczone rodziny
    def catch_selected_family(self):

        selected = self.driver.find_elements(*Locators.selected)
        families = []

        for i in selected:
            family = i.text
            families.append(family)
        #Zamiana listy na zbiór
        families = set(families)

        return families





