import os
from pprint import pprint
from flight_data import FlightData
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._base_url = "https://api.sheety.co/8e0786d81f21cf9fc793c51f1eead161/flightDeals/prices"
        self._header = {"Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"}
        self.flight_data = FlightData()

    def receive_sheet_info(self, should_print=True):
        response = requests.get(url=self._base_url, headers=self._header)
        if should_print:
            pprint(response.json(), width=120)
        return response.json()

    def update_iata_code(self):
        prices = self.receive_sheet_info(should_print=False)["prices"]
        for row in prices:
            row["iataCode"] = self.flight_data.get_location_query(row["city"])
            params = {"price": row}
            self.update_sheet_info(row["id"], params)

    def update_sheet_info(self, index_id, params):
        resp = requests.put(url=f"{self._base_url}/{index_id}", headers=self._header, json=params)
        pprint(resp.json(), width=120)
