import datetime
from abc import ABC, abstractmethod

import group


class Course(ABC):
    """
        Represents course interface.

        ...

        Attributes:
        ----------
            name : str
                title of the course.
            date : datetime
                course starting date.
            seminars_number : int
                number of seminars in the course.
            fee : float
                course fee.
            group_id_list : []
                contain group's id.

        Methods:
        --------
            add_group()
                Stands for adding group to the course.
            remove_group()
                Stands for removing group from the course
            send_course_materials()
                Diffuse some course material.
        """

    def __init__(self, id_: int, title: str, starting_date: datetime,
                 seminars_number: int, fee: float):
        self.id = id_
        self.title = title
        self.starting_date = starting_date
        self.seminars_number = seminars_number
        self.fee = fee
        self.group_id_list = []

    def __str__(self):
        return f"Current course name is {self.title} \n" \
               f"Course starts {self.starting_date} \n" \
               f"Number of seminars {self.seminars_number} \n" \
               f"The fee is {self.fee}"

    @abstractmethod
    def add_group(self, group_id: int) -> None:
        self.group_id_list.append(group_id)

    @abstractmethod
    def remove_group(self, group_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.group_id_list):
            if group_id == group_id:
                idx = i
                break
        del self.group_id_list[idx]

    @abstractmethod
    def send_course_materials(self, group: group.Group) -> None:
        group_id = group.group_id
        material = f"Some material for group - {group_id}"
        return print(material)


class DesignPatterns(Course):
    """
        Represents DesignPatterns course.

        ...

        Attributes:
        ----------
            id : int
                course id.
            title : str
                title of the course.
            date : datetime
                course starting date.
            seminars_number : int
                number of seminars in the course.
            fee : float
                course fee.

        Methods:
        --------
            add_group()
                Stands for adding group to the course.
            remove_group()
                Stands for removing group from the course
            send_course_materials()
                Diffuse some course material.
        """

    def __init__(self, id_: int, title: str, starting_date: datetime, seminars_number: int, fee: float):
        super().__init__(id_, title, starting_date, seminars_number, fee)

    def add_group(self, group_id) -> None:
        self.group_id_list.append(group_id)
        return print(f"Group - {group_id} was enrolled into Design Patterns")

    def remove_group(self, group_id) -> None:
        idx = 0
        for i, student in enumerate(self.group_id_list):
            if group_id == group_id:
                idx = i
                break
        del self.group_id_list[idx]
        return print(f"Group - {group_id} was removed from Design Patterns")

    def send_course_materials(self, group: group.Group) -> None:
        group_id = group.group_id
        material = f"Some material from Design Patterns for group - {group_id}"
        return print(material)


class MachineLearning(Course):
    """
        Represents MachineLearning course.

        ...

        Attributes:
        ----------
            id : int
                course id.
            title : str
                title of the course.
            date : datetime
                course starting date.
            seminars_number : int
                number of seminars in the course.
            fee : float
                course fee.

        Methods:
        --------
            add_group()
                Stands for adding group to the course.
            remove_group()
                Stands for removing group from the course
            send_course_materials()
                Diffuse some course material.
        """

    def __init__(self, id_: int, title: str, starting_date: datetime, seminars_number: int, fee: float):
        super().__init__(id_, title, starting_date, seminars_number, fee)

    def add_group(self, group_id) -> None:
        self.group_id_list.append(group_id)
        return print(f"Group - {group_id} was enrolled into Machine Learning")

    def remove_group(self, group_id) -> None:
        idx = 0
        for i, student in enumerate(self.group_id_list):
            if group_id == group_id:
                idx = i
                break
        del self.group_id_list[idx]
        return print(f"Group - {group_id} was removed from Machine Learning")

    def send_course_materials(self, group: group.Group) -> None:
        group_id = group.group_id
        material = f"Some material Machine Learning for group - {group_id}"
        return print(material)


class Calculus(Course):
    """
        Represents Calculus course.

        ...

        Attributes:
        ----------
            id : int
                course id.
            title : str
                title of the course.
            date : datetime
                course starting date.
            seminars_number : int
                number of seminars in the course.
            fee : float
                course fee.

        Methods:
        --------
            add_group()
                Stands for adding group to the course.
            remove_group()
                Stands for removing group from the course
            send_course_materials()
                Diffuse some course material.
        """

    def __init__(self, id_: int, title: str, starting_date: datetime, seminars_number: int, fee: float):
        super().__init__(id_, title, starting_date, seminars_number, fee)

    def add_group(self, group_id) -> None:
        self.group_id_list.append(group_id)
        return print(f"Group {group_id} was enrolled into Calculus")

    def remove_group(self, group_id) -> None:
        idx = 0
        for i, student in enumerate(self.group_id_list):
            if group_id == group_id:
                idx = i
                break
        del self.group_id_list[idx]
        return print(f" Group {group_id} was removed from Calculus")

    def send_course_materials(self, group: group.Group) -> None:
        group_id = group.group_id
        material = f"Some material Machine Learning for group {group_id}"
        return print(material)
