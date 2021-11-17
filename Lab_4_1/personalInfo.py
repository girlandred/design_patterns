import datetime
from dataclasses import dataclass


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: str
    employed_year: datetime
