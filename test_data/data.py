from faker import Faker
import csv
import json
import os

class TestData:

    def Faker(self):
        "Import faker library using polish datas"
        f = Faker(["pl_PL"])
        return f

    def ValidOrderNR(self):
        "Get valid OrderNr from .json file"
        file_path = os.path.join(os.path.dirname(__file__), '../test_data/orderNr.json')

        with open(file_path) as json_file:
            data = json.load(json_file)
        validOrderNr = data["ValidOrderNr"]

        return validOrderNr

    def get_alerts(self):
        "get alerts list data from csv file"
        alerts = []

        file_path = os.path.join(os.path.dirname(__file__), '../test_data/alerts.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                alerts.append(row[1])

        return alerts

    def get_wrong_emails(self):
        "get wrong emails from csv file"
        wrong_emails = []

        file_path = os.path.join(os.path.dirname(__file__), '../test_data/wrongEmail.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                wrong_emails.append(row)

        return wrong_emails



