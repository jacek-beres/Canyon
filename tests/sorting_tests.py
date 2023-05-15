from tests.base_test import BaseTest

class SortingPricesTest(BaseTest):
    def test_road_bikes_sorted_by_price_asc(self):

        roadbikes_page_object = self.home_page_object.select_road_bikes()
        roadbikes_page_object.click_product_filters()
        roadbikes_sorted_page_object = roadbikes_page_object.sort_by_price_acs()
        roadbikes_sorted_page_object.show_more_items()
        roadbikes_sorted_page_object.catch_all_prices()

        print(len(roadbikes_sorted_page_object.catch_all_prices()))
        self.assertEqual(len(roadbikes_sorted_page_object.catch_all_prices()), 59)
        #Sprawdzenie czy lista jest zgodna z listą posortowaną rosnąco
        self.assertEqual(roadbikes_sorted_page_object.catch_all_prices(), sorted(roadbikes_sorted_page_object.catch_all_prices()))

    def test_road_bikes_sorted_by_price_desc(self):

        roadbikes_page_object = self.home_page_object.select_road_bikes()
        roadbikes_page_object.click_product_filters()
        roadbikes_sorted_page_object = roadbikes_page_object.sort_by_price_desc()
        roadbikes_sorted_page_object.show_more_items()
        roadbikes_sorted_page_object.catch_all_prices()
        print(len(roadbikes_sorted_page_object.catch_all_prices()))
        self.assertEqual(len(roadbikes_sorted_page_object.catch_all_prices()), 59)

        #Sprawdzenie czy lista jest zgodna z listą posortowaną malejąco
        self.assertEqual(roadbikes_sorted_page_object.catch_all_prices(), sorted(roadbikes_sorted_page_object.catch_all_prices(), reverse=True))










