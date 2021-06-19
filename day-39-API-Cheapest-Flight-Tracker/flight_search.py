import requests
from datetime import datetime, timedelta
from flight_data import FlightData
import os


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self) -> None:
        self.KIWI_API = "https://tequila-api.kiwi.com"
        self.headers = {
            "apikey": os.environ['KIWI_API_KEY'],
            "accept": "application/json",
        }
        self.date_from = datetime.now().date()
        self.date_from_str = self.date_from.strftime('%d/%m/%Y')
        self.date_to = (datetime.today().date() + timedelta(weeks=24))
        self.date_to_str = self.date_to.strftime('%d/%m/%Y')
        self.city_from = "BER"
        self.city_to = "CAI"

    def get_city_code(self, city_name):
        parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": "true",
        }
        reponse = requests.get(url= f"{self.KIWI_API}/locations/query", params=parameters, headers=self.headers)
        reponse.raise_for_status()
        data = reponse.json()
        city_code = data["locations"][0]["code"]
        return city_code

    def search_cheapest_flights(self, city_from=None, city_to=None, date_from=None, date_to=None):
        parameters = {
            "fly_from": f"city:{city_from or self.city_from}",
            "fly_to": f"city:{city_to or self.city_to}",
            "date_from": f"{date_from or self.date_from_str}",
            "date_to": f"{date_to or self.date_to_str}",
            "curr": "EUR",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            # "one_for_city": 1,
        }
        reponse = requests.get(url=f"{self.KIWI_API}/v2/search", params=parameters, headers=self.headers)
        reponse.raise_for_status()
        flight_search_data = reponse.json()['data']
        try:
            data = flight_search_data[0]
        except IndexError:
            print(f"No flights from {city_from or self.city_from} to {city_to or self.city_to}")
            return None
        
        flight_data = FlightData(
            price=data.get('price'),
            origin_city=data.get('cityFrom'),
            origin_airport=data.get('flyFrom'),
            destination_city=data.get('cityTo'),
            destination_airport=data.get('flyTo'),
            out_date=data.get('route')[0].get('local_departure'),
            return_date=data.get('route')[-1].get('local_departure'),
            booking_link=data.get('deep_link')
        )

        return flight_data