import datetime
from typing import List


class CourseInformation:

    def __init__(self, id_: int, title: str, starting_date: datetime,
                 seminars_number: int, fee: float):
        self.id = id_
        self.title = title
        self.starting_date = starting_date
        self.seminars_number = seminars_number
        self.fee = fee

    def __str__(self):
        return f"Current course name is {self.title}..." \
               f"Course starts {self.starting_date}" \
               f"Number of seminars {self.seminars_number}" \
               f"The fee is {self.fee}"


class Course:
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

    def __init__(self, course_info: CourseInformation):
        self.course_info = course_info
        self.student_id_list = []

    def add_student(self, student_id: int) -> None:
        self.student_id_list.append(student_id)

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.student_id_list):
            if student.id == student_id:
                idx = i
                break
        del self.student_id_list[idx]

    def __str__(self):
        return f"{self.course_info.title}"


class Seminar:

    def __init__(self, id_: int, title: str,
                 deadline: datetime, items: List[str],
                 status: float, related_course: str):
        self.id = id_
        self.title = title
        self.deadline = deadline
        self.items = items
        self.status = status
        self.related_course = related_course

    def implement_item(self, item_name: str) -> str:
        if item_name in self.items:
            return f"{item_name} has been implemented"

    def add_comment(self, message: str, person) -> None:
        person.comments.append(f'{self.title}: {message}')


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

    def add_student(self, student_id: int) -> None:
        self.student_id_list.append(student_id)
        return print(f"Student {student_id} was enrolled into Calculus")

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.student_id_list):
            if student_id == student_id:
                idx = i
                break
        del self.student_id_list[idx]
        return print(f" Student {student_id} was removed from Calculus")

    def send_course_materials(self) -> None:
        material = f"Some material Machine Learning for group"
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

    def add_student(self, student_id: int) -> None:
        self.student_id_list.append(student_id)
        return print(f"Student {student_id} was enrolled into Calculus")

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.student_id_list):
            if student_id == student_id:
                idx = i
                break
        del self.student_id_list[idx]
        return print(f" Student {student_id} was removed from Calculus")

    def send_course_materials(self) -> None:
        material = f"Some material Machine Learning for group"
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

    def add_student(self, student_id: int) -> None:
        self.student_id_list.append(student_id)
        return print(f"Student {student_id} was enrolled into Calculus")

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.student_id_list):
            if student_id == student_id:
                idx = i
                break
        del self.student_id_list[idx]
        return print(f" Student {student_id} was removed from Calculus")

    def send_course_materials(self) -> None:
        material = f"Some material Machine Learning for group"
        return print(material)
