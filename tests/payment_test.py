from tests.base_test import BaseTest

class MonthlyPayment(BaseTest):

    def test_monthly_payment(self):
        #Test wykonujemy dla każdej z 5 zakładek na stronie
        tabs = self.home_page_object.bikes_tabs()

        for i in range(len(tabs)):
            # Problem: szybkie wykonywaniem kodu i próbą odwołania się do nieistniejących elementów (stale element reference).
            # Rozwiązaniem jest ponowne pobranie listy elementów przed każdą iteracją pętli.
            tabs = self.home_page_object.bikes_tabs()
            bikes_page_object = self.home_page_object.click_tab(tabs[i])
            bikes_page_object.show_more_items()
            prices = bikes_page_object.catch_all_prices()
            monthly_prices = bikes_page_object.catch_monthly_prices()

            #Sprawdzenie, czy lista z cenami ma taką samą długość jak z cenami ratalnymi
            self.assertEqual(len(prices), len(monthly_prices))

            for i in range(len(monthly_prices)):
                price = prices[i]
                monthly_price = monthly_prices[i]
                # Producent zapewnie rozłożenie płatności na 6 równych rat
                # Sprawdzenie, czy każdy element z listy 'monthly_prices' odpowiada co do wartości 1/6 odpowiadającemu elementowi z listy 'prices'
                # Dodano tolerancję 0,5% ze względu na błąd zaokrągleń
                self.assertAlmostEqual(monthly_price, price / 6, delta=(price / 6)*0.005)

            bikes_page_object.go_to_top()


