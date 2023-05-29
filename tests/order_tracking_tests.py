from tests.base_test import BaseTest
from test_data.data import TestData
from ddt import ddt, data, unpack

dane = TestData()
alerts = dane.get_alerts()
f = dane.Faker()
validON = dane.ValidOrderNR()
wrong_emails = dane.get_wrong_emails()

@ddt
class OrderTracking(BaseTest):

    def setUp(self):
        "W testach śledzenia zamówienia stroną główną jest strona śledzenia zamówenia (OrderTrackingPage)"

        super().setUp()
        self.home_page_object.click_head()
        self.order_tracking_page_object = self.home_page_object.go_to_order_page()

    def test_TC1_1(self):
        "Email - brak, nr zamówienia: brak"

        #Nie wpisujemy danych do sledzenia zamowienia,od razu klimamy "zatwiedź'
        self.order_tracking_page_object.click_next()

        #Sprawdzenie czy alert maila jest widoczny i przy mailu i numerze zamowienia wyswietla sie stosowny komunikat
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_email_message().text)
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_order_nr_message().text)

    def test_TC1_2(self):
        "Email - brak, nr zamówienia: nieprawdiłowy"

        # Wpisujemy tylko zły numer zamówienia
        self.order_tracking_page_object.enter_order_nr(f.phone_number())
        self.order_tracking_page_object.click_next()

        #Sprawdzenie czy alert maila jest widoczny i przy mailu i numerze zamowienia wyswietla sie stosowny komunikat
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(self.order_tracking_page_object.catch_order_nr_message())

    def test_TC1_3(self):
        "Email - brak, nr zamówienia: prawdiłowy"

        # Wpisujemy tylko zły numer zamówienia
        self.order_tracking_page_object.enter_order_nr(validON)
        self.order_tracking_page_object.click_next()

        #Sprawdzenie czy alert maila jest widoczny i przy mailu i numerze zamowienia wyswietla sie stosowny komunikat
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(self.order_tracking_page_object.catch_order_nr_message())

    @data(*wrong_emails)
    @unpack
    def test_TC1_4(self, wrong_email):
        "Email: nieprawdiłowy format, Nr zamówienia: brak"

        # Wpisujemy tylko złego maila"
        self.order_tracking_page_object.enter_email(wrong_email)
        self.order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(alerts[1], self.order_tracking_page_object.catch_email_message().text)
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_order_nr_message().text)

    @data(*wrong_emails)
    @unpack
    def test_TC1_5(self, wrong_email):
        "Email: nieprawdiłowy format, Nr zamówienia: nieprawidłowy"

        # Wpisujemy złego maila, zły nr zamowienia, klimamy "zatwiedź' "
        self.order_tracking_page_object.enter_email(wrong_email)
        self.order_tracking_page_object.enter_order_nr(f.phone_number())
        self.order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(alerts[1], self.order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(self.order_tracking_page_object.catch_order_nr_message())

    @data(*wrong_emails)
    @unpack
    def test_TC1_6(self, wrong_email):
        "Email: nieprawdiłowy format, Nr zamówienia: prawidłowy"

        #email leci z ddt, nr zamówienia z .jsona
        self.order_tracking_page_object.enter_email(wrong_email)
        self.order_tracking_page_object.enter_order_nr(validON)
        self.order_tracking_page_object.click_next()
        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(alerts[1], self.order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(self.order_tracking_page_object.catch_order_nr_message())

    def test_TC1_7(self):
        "Email: prawdiłowy format, ale brak w bazie, Nr zamówienia: brak"

        # Nie wpisujemy danych do sledzenia zamowienia,od razu klimamy "zatwiedź' "
        self.order_tracking_page_object.enter_email(f.email())
        self.order_tracking_page_object.click_next()

        #Oczekiwane zachowanie: brak pola alertu dla maila, i pole alertu w wiadomością
        self.assertIsNone(self.order_tracking_page_object.catch_email_message())
        self.assertEqual(alerts[0], self.order_tracking_page_object.catch_order_nr_message().text)

    def test_TC1_8(self):
        "Email: prawdiłowy format, Nr zamówienia: nieprawidłowy"
        # Wpisujemy maila i złe dane do sledzenia zamowienia: (nr telefonu) "
        self.order_tracking_page_object.enter_email(f.email())
        self.order_tracking_page_object.enter_order_nr(f.phone_number())
        self.order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertIsNone(self.order_tracking_page_object.catch_email_message())
        self.assertEqual(alerts[2], self.order_tracking_page_object.catch_order_nr_message().text)

    def test_TC1_9(self):
        "Email: poprawny format, Nr zamówienia: prawidłowy"
        # Wpisujemy złego maila bez numeru, od razu klimamy "zatwiedź' "
        self.order_tracking_page_object.enter_email(f.email())
        self.order_tracking_page_object.enter_order_nr(validON)
        self.order_tracking_page_object.click_next()

        # Oczekiwane zachowanie: brak pola alertu dla maila, pole alertu w wiadomością
        self.assertEqual(alerts[3], self.order_tracking_page_object.catch_email_message().text)
        self.assertIsNone(self.order_tracking_page_object.catch_order_nr_message())








