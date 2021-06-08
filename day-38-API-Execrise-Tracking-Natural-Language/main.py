import requests
import os
from datetime import datetime


NUTRI_API_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_API_KEY = os.environ["API_KEY"]
NUTRI_APP_ID = os.environ["APP_ID"]

if not NUTRI_API_KEY and not NUTRI_APP_ID:
    exit("Keys were not found in env")

user_input = input("Tell me what did you excersise today: ")

nutri_headers = {  
    "x-app-key": NUTRI_API_KEY,
    "x-app-id": NUTRI_APP_ID,
}

nutri_parameters = {
 "query": user_input,
 "gender": "male",
 "weight_kg": 70.5,
 "height_cm": 183.64,
 "age": 30
}


SHEET_URL = os.environ["SHEET_URL"]
SHEET_TOKEN = os.environ["SHEET_TOKEN"]

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

workouts = {
   "workout": {

   }
}


def analyze_workout():
    response = requests.post(url=NUTRI_API_ENDPOINT, json=nutri_parameters, headers=nutri_headers)
    response.raise_for_status()
    data = response.json()

    for exercise in data["exercises"]:                    
        workouts["workout"]['date'] = datetime.today().strftime("%d/%m/%Y")
        workouts["workout"]['time'] = datetime.now().strftime('%H:%M:%S')
        workouts["workout"]['exercise'] = exercise["name"].title()
        workouts["workout"]['duration'] = exercise["duration_min"]
        workouts["workout"]['calories'] = exercise["nf_calories"]
        save_to_worksheet()


def retrieve_worksheet():
    response = requests.get(url=SHEET_URL, headers=sheet_headers)
    response.raise_for_status()
    data = response.json()
    print(data)
    

def save_to_worksheet():    
    response = requests.post(url=SHEET_URL, json=workouts, headers=sheet_headers)
    print(response.text)
    response.raise_for_status()


retrieve_worksheet()
analyze_workout()
retrieve_worksheet()
