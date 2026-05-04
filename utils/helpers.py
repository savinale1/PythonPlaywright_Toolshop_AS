import datetime
from calendar import month
from dataclasses import dataclass
from faker import Faker


@dataclass

class RegisterUserData:
    first_name : str
    last_name : str
    birth_date : str
    email : str
    password : str
    phone_number: str

def generate_user_registration_data():
    f = Faker()
    return RegisterUserData(
        first_name = f.first_name_female(),
        last_name = f.last_name(),
        birth_date = f.date_of_birth(minimum_age=19, maximum_age=90).strftime("%Y-%m-%d"),
        email = f.email(),
        password = f.password(8),
        phone_number=f.numerify("##########")
    )

@dataclass
class AddressData:
    country: str
    zip: str
    building: str
    street: str
    city: str
    state: str

def generate_address_data():
    f = Faker()
    return AddressData(
        country = "US",
        zip=f.zipcode(),
        building = "123",
        street = f.street_address(),
        city = f.city(),
        state = f.state(),
    )