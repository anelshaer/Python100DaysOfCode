from flight_search import FlightSearch
from data_manager import DataManager
from requests import exceptions as reqExceptions
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

ORIGIN_CITY_IATA = "BER"


def update_city_codes(cities):
    for city in cities['prices']:
        update_row = {'price': {}}
        updated_city = update_row['price']
        if city.get('iataCode') == '':
            updated_city['city'] = city['city']
            updated_city['iataCode'] = (fsearch.get_city_code(city['city']))
            updated_city['lowestPrice'] = city['lowestPrice']
            dmanager.update_city(city['id'], update_row)


fsearch = FlightSearch()

dmanager = DataManager()
notification = NotificationManager()
sheet_data = dmanager.get_cities()
# sheet_data = {'prices': [
#     {'city': 'Cairo', 'iataCode': 'CAI', 'lowestPrice': 500, 'id': 2},
#     {'city': 'Amsterdam', 'iataCode': 'AMS', 'lowestPrice': 200, 'id': 3},
#     {'city': 'Frankfurt ', 'iataCode': 'FRA', 'lowestPrice': 100, 'id': 4},
#     {'city': 'Bonn', 'iataCode': 'CGN', 'lowestPrice': 150, 'id': 7},
#     {'city': 'Lübeck', 'iataCode': 'LBC', 'lowestPrice': 400, 'id': 8},
#     {'city': 'Prague', 'iataCode': 'PRG', 'lowestPrice': 100, 'id': 9}
#     ]
# }

update_city_codes(sheet_data)

for city_data in sheet_data['prices']:
    try:
        flight_data = fsearch.search_cheapest_flights(city_from=ORIGIN_CITY_IATA, city_to=city_data['iataCode'])
        if flight_data and flight_data.price <= city_data.get('lowestPrice'):
            notification.send_sms(f"Low price alert! {flight_data}")
            print(f"Low price alert! {flight_data}")
    except reqExceptions.HTTPError as e:
        print(f"Error encountered: {e}")