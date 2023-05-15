from tests.base_test import BaseTest

class SortingPricesTest(BaseTest):
    def test_road_bikes_sorted_by_price_asc(self):

        tabs = self.home_page_object.bikes_tabs()

        for tab in tabs:
            print('zakładka ', tab.text, ' załadowana poprawnie')
            roadbikes_page_object = self.home_page_object.click_tab(tab)
            prices = roadbikes_page_object.catch_all_prices()
            monthly_prices = roadbikes_page_object.catch_monthly_prices()

            # Producent zapewnie rozłożenie płatności na 6 równych rat
            # Sprawdzenie, czy każdy element z listy 'monthly_prices' odpowiada co do wartości 1/6 odpowiadającemu elementowi z listy 'prices'
            # Dodano tolerancję 0,5% ze względu na błąd zaokrągleń

            for i in range(len(monthly_prices)):
                price = prices[i]
                monthly_price = monthly_prices[i]
                self.assertAlmostEqual(monthly_price, price / 6, delta=0.005)

            roadbikes_page_object.return_home_page()



            #
            # print('zakładka ', tab.text, ' załadowana poprawnie')
            #
            # roadbikes_page_object = self.home_page_object.click_tab(tab)
            # prices = roadbikes_page_object.catch_all_prices()
            # monthly_prices = roadbikes_page_object.catch_monthly_prices()
            #
            # #Producent zapewnie rozłożenie płatności na 6 równych rat
            # #Sprawdzenie, czy każdy element z listy 'monthly_prices' odpowiada co do wartości 1/6 odpowiadającemu elementowi z listy 'prices'
            # #Dodano tolerancję 0,5% ze względu na błąd zaokrągleń
            #
            # for i in range(len(monthly_prices)):
            #     price = prices[i]
            #     monthly_price = monthly_prices[i]
            #     self.assertAlmostEqual(monthly_price, price / 6, delta=0.005)
            #
            # print(tab.text, 'wykonana poprawnie')