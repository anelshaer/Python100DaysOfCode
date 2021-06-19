from dataclasses import dataclass


@dataclass
class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, booking_link):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.booking_link = booking_link

    def __repr__(self):        
        return f"{self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport} €{self.price} From:{self.out_date.split('T')[0]} To:{self.return_date.split('T')[0]}"