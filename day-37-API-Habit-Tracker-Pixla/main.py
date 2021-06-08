import requests
import os
import random
from datetime import datetime, timedelta
import time


pixela_endpoint = "https://pixe.la/v1/users"
Username = os.environ["PIXLA_USERNAME"]
token = os.environ["PIXLA_TOKEN"]
id = "graph6610"

headers = {
    "X-USER-TOKEN": token
}


def create_account():
    parameters = {
        "token": token,
        "username": Username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    print(parameters)
    response = requests.post(url=pixela_endpoint, json=parameters)
    print(f"Account Creation: {response.text}")
    response.raise_for_status()


def create_graph(graph_name, unit):
    id = f"graph{random.randint(10, 9999)}"

    parameters = {
        "id": id,
        "name": graph_name,
        "unit": unit,
        "type": "float",
        "color": "sora",
    }

    response = requests.post(url=f"{pixela_endpoint}/{Username}/graphs", json=parameters, headers=headers)    
    print(f"Graph Creation: {response.text}")
    response.raise_for_status()
    return id


def create_pixel(graph_id, date, quantity):    
    parameters = {
        "date": date,
        "quantity": quantity,
    }
    reponse = requests.post(url=f"{pixela_endpoint}/{Username}/graphs/{graph_id}", json=parameters, headers=headers)
    print(f"Creating Pixel: graph: {graph_id} Date: {date} Quantity: {quantity}")
    reponse.raise_for_status()


def update_pixel(graph_id, date, quantity):
    parameters = {
        "quantity" : quantity,
    }
    response = requests.put(url=f"/{Username}/graphs/{id}/{date}", json=parameters, headers=headers)
    print(f"Changing Pixel: graph: {graph_id} Date: {date} Quantity: {quantity}")
    response.raise_for_status()


def delete_pixel(graph_id, date):
    response = requests.delete(url=f"/{Username}/graphs/{id}/{date}", headers=headers)
    print(f"Deleting Pixel: graph: {graph_id} Date: {date}")
    response.raise_for_status()


#creating a year of random pixels
for day in range(1, 365):
    date = datetime.today().date() - timedelta(days=day)
    str_date = date.strftime('%Y%m%d')
    random_quantity = str(random.randint(0, 100))
    create_pixel(id, str_date, random_quantity)
    time.sleep(0.5)
