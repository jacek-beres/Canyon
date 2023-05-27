import unittest
from tests.payment_test import MonthlyPayment
from tests.order_tracking_tests import OrderTracking
from tests.sorting_tests import SortingPricesTest
import xmlrunner

# Pobranie testów do uruchomienia
order_tracking_tests = unittest.TestLoader().loadTestsFromTestCase(OrderTracking)
payment_test = unittest.TestLoader().loadTestsFromTestCase(MonthlyPayment)
sorting_tests = unittest.TestLoader().loadTestsFromTestCase(SortingPricesTest)

# Lista testów
tests_for_run = [
    order_tracking_tests,
    payment_test,
    sorting_tests
]

# Suite'a
test_suite = unittest.TestSuite(tests_for_run)

# Utwórz obiekt runnera xmlrunner
runner = xmlrunner.XMLTestRunner(output='test_reports')

# Odpal testy przy użyciu runnera
runner.run(test_suite)