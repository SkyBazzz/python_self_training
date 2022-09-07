"""
https://www.nutritionix.com/business/api
https://dashboard.sheety.co/projects/62b5d3e0c9e9ac0a39347d52/sheets/workouts
https://docs.google.com/spreadsheets/d/1tzhzPzZmF5Z0CZtHGJ2srf442j_Fo_DYJJfeqkjSDfE/edit#gid=0
"""
import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shitty_add = "https://api.sheety.co/8e0786d81f21cf9fc793c51f1eead161/workoutTracking/workouts"

headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
}

workout = "walk 30km, run 10km"  # input("Tell me which exercise you did: ")
params = {
    "query": workout,
    "gender": "male",
    "weight_kg": 74,
    "height_cm": 179,
    "age": 29,
}
response = requests.post(url=exercise_endpoint, headers=headers, json=params)
exercises = response.json()["exercises"]
print(exercises)

shitty_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}",
    "Content-Type": "application/json"
}

for exercise in exercises:
    template = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    resp = requests.post(url=shitty_add, headers=shitty_headers, json=template)
    print(resp.text)
