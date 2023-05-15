from tests.base_test import BaseTest
from time import sleep

class FilterTests(BaseTest):
    def test_filtering_family(self):

        roadbikes_page_object = self.home_page_object.select_road_bikes()
        roadbikes_page_object.show_filters()
        roadbikes_page_object.expand_family()
        set_a = roadbikes_page_object.catch_family_name()
        bikes_filtered_page_object = roadbikes_page_object.click_family()

        set_b = bikes_filtered_page_object.catch_model_names()

        print(set_b)
        print(set_a)

        self.assertTrue(set_b.issubset(set_a))


