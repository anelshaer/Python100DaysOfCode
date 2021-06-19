import requests
import os


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    
    def __init__(self) -> None:
        self.SHEETY_URL = os.environ["SHEETY_URL"]
        self.sheet_data = {}
        self.bearer_token = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }

    def get_cities(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.headers)
        response.raise_for_status()
        self.sheet_data = response.json()
        return self.sheet_data
        
    def update_city(self, row_id, city_data):
        self.headers["Content-Type"] = "application/json"           
        response = requests.put(url=f"{self.SHEETY_URL}/{row_id}", json=city_data,headers=self.headers)
        response.raise_for_status()        
