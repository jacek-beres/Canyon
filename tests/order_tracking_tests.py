from tests.base_test import BaseTest
from time import sleep
import json
from faker import Faker

f = Faker(["pl_PL"])

expected_alert1 = "Prosimy o odpowiedź tutaj."
expected_alert2 = "Wprowadzone dane nie są zgodne z wymaganiami."
expected_alert3 = "Nieprawidłowy numer zamówienia"
expected_alert4 = 'Niezgodność adresu e-mail z nr. zamówienia.'
valid_order_number = '9401083657'

class OrderTracking(BaseTest):

    # with open(test.data.'alerts.json', 'r') as f:
    #     data = json.load(f)

    def test_NoEmailNoOrderNR(self):
        "W tym teście nie wpisujemy ani maila, ani numeru zamównienia, sprawdzane są alerty"

        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        #Nie wpisujemy danych do sledzenia zamowienia,od razu klimamy "zatwiedź'
        order_tracking_page_object.click_next()

        #Sprawdzenie czy alert maila jest widoczny i przy mailu i numerze zamowienia wyswietla sie stosowny komunikat
        self.assertEqual(expected_alert1, order_tracking_page_object.catch_email_message().text)
        self.assertEqual(expected_alert1, order_tracking_page_object.catch_order_nr_message().text)

    def test_EmailNoOrderNR(self):
        "W tym teście wpisujemy tylko maila, bez numeru zamównienia, sprawdzane są alerty"

        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        # Nie wpisujemy danych do sledzenia zamowienia,od razu klimamy "zatwiedź' "
        order_tracking_page_object.enter_email(f.email())
        order_tracking_page_object.click_next()

        #Oczekiwane zachowanie: brak pola alertu dla maila, i pole alertu w wiadomością
        self.assertIsNone(order_tracking_page_object.catch_email_message())
        self.assertEqual(expected_alert1, order_tracking_page_object.catch_order_nr_message().text)

    def testEmailFakeOrderPR(self):
        "W tym teście wpisujemy tylko maila, z niepoprawnym numerem zamowienia, sprawdzane są alerty"
        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        # Wpisujemy maila i złe dane do sledzenia zamowienia, od razu klimamy "zatwiedź' "
        order_tracking_page_object.enter_email(f.email())
        order_tracking_page_object.enter_order_nr(f.phone_number())
        order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertIsNone(order_tracking_page_object.catch_email_message())
        self.assertEqual(expected_alert3, order_tracking_page_object.catch_order_nr_message().text)

    def testWrongEmailNoOrderPR(self):
        "W tym teście wpisujemy tylko maila, z niepoprawnym numerem zamowienia, sprawdzane są alerty"

        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        # Wpisujemy złego maila bez numeru, od razu klimamy "zatwiedź' "
        order_tracking_page_object.enter_email(f.name())
        order_tracking_page_object.enter_order_nr(f.phone_number())
        order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(expected_alert2, order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(order_tracking_page_object.catch_order_nr_message())


    def testWrongEmailOrderPR(self):
        "W tym teście wpisujemy złego maila, z poprawnym numerem zamowienia, sprawdzane są alerty"

        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        # Wpisujemy złego maila bez numeru, od razu klimamy "zatwiedź' "
        order_tracking_page_object.enter_email(f.name())
        order_tracking_page_object.enter_order_nr(valid_order_number)
        order_tracking_page_object.click_next()
        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(expected_alert2, order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(order_tracking_page_object.catch_order_nr_message())

    def testFakeEmailOrderPR(self):
        "W tym teście wpisujemy złego maila, z poprawnym numerem zamowienia, sprawdzane są alerty"

        self.home_page_object.click_head()
        order_tracking_page_object = self.home_page_object.go_to_order_page()
        # Wpisujemy złego maila bez numeru, od razu klimamy "zatwiedź' "
        order_tracking_page_object.enter_email(f.email())
        order_tracking_page_object.enter_order_nr(valid_order_number)
        order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(expected_alert4, order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(order_tracking_page_object.catch_order_nr_message())








