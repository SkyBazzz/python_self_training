# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    import requests

    resp = requests.get(url="https://russianwarship.rip/api/v1/statistics/latest")
    pprint(resp.json())
