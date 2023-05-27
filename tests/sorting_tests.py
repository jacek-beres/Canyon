from tests.base_test import BaseTest

class SortingPricesTest(BaseTest):
    def test_TC3_1(self):
    # Testy sortowania prouktów rosnąco na każdej z 5 zakładek
        tabs = self.home_page_object.bikes_tabs()

        for i in range(len(tabs)):

            # Problem: szybkie wykonywaniem kodu i próbą odwołania się do nieistniejących elementów (stale element reference).
            # Rozwiązaniem tego problemu jest ponowne pobranie listy elementów przed każdą iteracją pętli.

            tabs = self.home_page_object.bikes_tabs()
            bikes_page_object = self.home_page_object.click_tab(tabs[i])
            bikes_page_object.click_product_filters()
            bikes_sorted_page_object = bikes_page_object.sort_by_price_acs()
            bikes_sorted_page_object.catch_all_prices()

            # Sprawdzamy obie wersje - jeśli ceny są posortowane uwzględniająć BikeOfTheWeek (wyjęty spoza sortowania)
            # Spełniony musi być jeden z warunków
            products_asc = bikes_sorted_page_object.catch_all_sale_prices()
            products_asc_sale = bikes_sorted_page_object.catch_all_prices()
            self.assertTrue(products_asc == sorted(products_asc) or products_asc_sale == sorted(products_asc_sale))

            bikes_sorted_page_object.go_to_top()

    def test_TC3_2(self):
    # Testy sortowania prouktów malejąco na każdej z 5 zakładek
        tabs = self.home_page_object.bikes_tabs()

        for i in range(len(tabs)):
            # Problem: szybkie wykonywaniem kodu i próbą odwołania się do nieistniejących elementów (stale element reference).
            # Rozwiązaniem tego problemu jest ponowne pobranie listy elementów przed każdą iteracją pętli.

            tabs = self.home_page_object.bikes_tabs()
            bikes_page_object = self.home_page_object.click_tab(tabs[i])
            bikes_page_object.click_product_filters()
            bikes_sorted_page_object = bikes_page_object.sort_by_price_desc()
            bikes_sorted_page_object.catch_all_prices()

            #Sprawdzamy obie wersje - jeśli ceny są posortowane uwzględniająć BikeOfTheWeek (wyjęty spoza sortowania)
            #Spełniony musi być jeden z warunków
            products_desc = bikes_sorted_page_object.catch_all_sale_prices()
            products_desc_sale = bikes_sorted_page_object.catch_all_prices()

            self.assertTrue(products_desc == sorted(products_desc, reverse=True) or products_desc_sale == sorted(products_desc_sale, reverse=True))

            bikes_sorted_page_object.go_to_top()











