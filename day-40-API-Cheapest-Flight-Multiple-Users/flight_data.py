from dataclasses import dataclass


@dataclass
class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city,
                 destination_airport, out_date, return_date, booking_link,
                 stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.booking_link = booking_link
        self.stop_over = stop_overs
        self.via_city = via_city

    def __repr__(self):
        string = f"{self.origin_city}-{self.origin_airport} to "
        string += f"{self.destination_city}-{self.destination_airport} "
        string += f"€{self.price} From:{self.out_date.split('T')[0]} "
        string += f"To:{self.return_date.split('T')[0]} "
        if self.stop_over > 0:        
            string += f"Flight has {self.stop_over} stop over via {self.via_city} City"

        string += f"Booking Link: {self.booking_link}\n"
        string += f"Google Flight Search: https://www.google.com/flights?hl=en#flt={self.origin_airport}.{self.destination_airport}.{self.out_date.split('T')[0]}*{self.destination_airport}.{self.origin_airport}.{self.return_date.split('T')[0]}"
        return string
