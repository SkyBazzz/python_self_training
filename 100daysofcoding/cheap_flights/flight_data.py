import os

import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self._base_url = "https://tequila-api.kiwi.com/"
        self._header = {"apikey": os.environ.get("TEQUILA_API_KEY")}

    def get_location_query(self, term):
        params = {"term": term}
        resp = requests.get(
            url=f"{self._base_url}{'locations/query'}",
            params=params,
            headers=self._header,
        )
        print(resp.json()["locations"][0]["code"])
        return resp.json()["locations"][0]["code"]
