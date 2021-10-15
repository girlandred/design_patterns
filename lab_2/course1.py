from datetime import datetime
from typing import List

from staff1 import Staff


class CourseInformation:

    def __init__(self, title: str, starting_date: datetime,
                 seminars_number: int, fee: float):
        self.title = title
        self.starting_date = starting_date
        self.seminars_number = seminars_number
        self.fee = fee


class Course:
    """
        Represents course taken in universities.

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

        Methods:
        --------
            add_student(student: Student)
                Stands for adding student to the course.
            remove_student(student: Student)
                Stands for removing student from the course
        """
    def __init__(self, id_: int, course_info: CourseInformation):
        self.id = id_
        self.course_info = course_info
        self.student_id_list = []
        self.seminar_list = []

    def add_student(self, student_id: int) -> None:
        self.student_id_list.append(student_id)

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.student_id_list):
            if student.id == student_id:
                idx = i
                break
        del self.student_id_list[idx]


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

    def add_comment(self, message: str, person: Staff) -> None:
        person.comments.append(f'{self.title}: {message}')
