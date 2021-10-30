import datetime
from dataclasses import dataclass


@dataclass
class PersonalInfo:
    """
        Represents personal information.

        ...

        Attributes:
        ----------
            id : int
                personal id
            name : str
                name of person.
            address : str
                person's address.
            phone_number : str
                show person's phone number.
            email : str
                contain data about email.
            position : str
                show person's position
            employed_year : datetime
                contain year when person was employed
        """
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: str
    employed_year: datetime
