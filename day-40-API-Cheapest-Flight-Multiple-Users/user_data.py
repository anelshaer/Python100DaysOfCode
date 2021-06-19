from dataclasses import dataclass


@dataclass
class UserData:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    def __repr__(self):        
        return f"Full Name: {self.first_name} {self.last_name}, Email: {self.email}"