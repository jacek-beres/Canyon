from tests.base_test import BaseTest

class SortingPricesTest(BaseTest):
    def test_road_bikes_sorted_by_price_asc(self):

        roadbikes_page_object = self.home_page_object.select_road_bikes()
        roadbikes_page_object.show_more_items()
        prices = roadbikes_page_object.catch_all_prices()
        monthly_prices = roadbikes_page_object.catch_monthly_prices()

        #Producent zapewnie rozłożenie płatności na 6 równych rat
        #Sprawdzenie, czy każdy element z listy 'monthly_prices' odpowiada co do wartości 1/6 odpowiadającemu elementowi z listy 'prices'
        #Dodano tolerancję 0,5% ze względu na błąd zaokrągleń

        for i in range(len(monthly_prices)):
            price = prices[i]
            monthly_price = monthly_prices[i]
            print(price, '        ', monthly_price)
            self.assertAlmostEqual(monthly_price, price / 6, delta=0.005)