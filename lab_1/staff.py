from typing import List

from lab_1.course import Course
from lab_1.enrollment import Enrollment


class Staff:
    """
    Represents staff.

    ...

    Attributes:
    ----------
        name : str
            name of staff member.
        address : str
            member's address.
        phone_number : str
            show staff member's phone number.
        email : str
            contain data about email.
    """

    def __init__(self, name: str, address: str,
                 phone_number: str, email: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Staff member {self.name}" \
               f"Address {self.address}" \
               f"Phone number {self.phone_number}" \
               f"Email {self.email}"


class Student(Staff):
    """
    Represents students

    ...

    Attributes:
    ----------
        id : int
            student's id.
        name : str
            student's name.
        address : str
            information about student's address.
        phone_number : str
            contain phone number.
        email : str
            student's email.
        student_number : int
            student's number

    Methods:
    --------

        can_enroll(seminar: Course)
            Define if student can enroll in course.
        taken_seminars()
            Contain information about taken course.
        enroll(course: Course)
            Add student into course
        unenroll(course: Course)
            Remove student from course
    """
    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str,
                 student_number: int):
        super(Student, self).__init__(name=name, address=address,
                                      phone_number=phone_number, email=email)
        self.id = id_
        self.student_number = student_number
        self.average_mark = 0.0
        self.enrollments = []

    def taken_seminars(self) -> List[Course]:
        courses = [enrollment.course
                   for enrollment in self.enrollments]

        return courses

    def can_enroll(self, course: Course) -> bool:
        if self.average_mark >= 4.5:
            return True

    def enroll(self, course: Course) -> None:
        course.add_student(student_id=self.id)
        enrollment = Enrollment(course=course)
        self.enrollments.append(enrollment)
        print(f'{self} has enrolled in {course}')

    def unenroll(self, course: Course) -> None:
        idx = 0
        for i, enrollment in enumerate(self.enrollments):
            if enrollment.course.id == course.id:
                idx = i
                break
        self.enrollments[idx].course.\
            remove_student(student_id=self.id)
        del self.enrollments[idx]

    def __str__(self):
        return f"Name: {self.name}..."


class Professor(Staff):
    """"
    Contain information about professor

    ...

    Attributes:
    ----------
        name : str
            professor's name.
        address : str
            information about professor's address.
        phone_number : str
            contain phone number.
        email : str
            student's email.
        salary : float
            professor's salary
        course : Course
            professor's course
    """

    def __init__(self, name: str, address: str, phone_number: str, email: str, salary: float,
                 course: Course):
        super(Professor, self).__init__(name=name, address=address,
                                        phone_number=phone_number, email=email)
        self.salary = salary
        self.course = course
