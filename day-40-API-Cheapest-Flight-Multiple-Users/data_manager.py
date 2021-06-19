import requests
import os
from user_data import UserData
import json


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self) -> None:
        self.SHEETY_URL = f"https://api.sheety.co/{os.environ['SHEETY_SHEET_ID']}/pythonFlightDeals"
        self.sheet_data = {}
        self.bearer_token = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }

    def get_cities(self):
        response = requests.get(url=f"{self.SHEETY_URL}/prices", headers=self.headers)
        response.raise_for_status()
        self.sheet_data = response.json()
        return self.sheet_data

    def update_city(self, row_id, city_data):
        self.headers["Content-Type"] = "application/json"
        response = requests.put(url=f"{self.SHEETY_URL}/prices/{row_id}", json=city_data,headers=self.headers)
        response.raise_for_status()        

    def get_users(self):
        response = requests.get(url=f"{self.SHEETY_URL}/subscribers", headers=self.headers)
        response.raise_for_status()
        return response.json()['subscribers']

    def add_user(self, user: UserData):
        self.headers["Content-Type"] = "application/json"
        user_data = {
            "subscriber": {
                "first": str(user.first_name),
                "last": str(user.last_name),
                "email": str(user.email),
            }
        }

        response = requests.post(url=f"{self.SHEETY_URL}/subscribers", json=user_data, headers=self.headers)
        print(response.text)
        response.raise_for_status()
