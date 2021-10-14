from dataclasses import dataclass
from datetime import datetime


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: str
    employed_year: datetime
