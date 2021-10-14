from typing import List
from abc import ABC, abstractmethod

from course1 import Course, Seminar
from enrollment1 import Enrollment
from personalInfo import PersonalInfo


class Staff(ABC):
    def __init__(self, _personal_info: PersonalInfo) -> None:
        self.enrollments = list()
        self.comments = None
        self._personal_info = _personal_info

    @property
    def _personal_info(self) -> PersonalInfo:
        return self._personal_info

    @_personal_info.setter
    def _personal_info(self, _personal_info: PersonalInfo) -> None:
        if isinstance(_personal_info, PersonalInfo):
            self._personal_info = PersonalInfo
        else:
            raise AttributeError(f"personal_info object must be of class Personal info")

    def taken_seminars(self) -> List[Course]:
        courses = [enrollment.course
                   for enrollment in self.enrollments]
        return courses

    @abstractmethod
    def can_enroll(self, course: Course) -> None:
        pass

    @abstractmethod
    def calculate_workload(self) -> float:
        pass

    @abstractmethod
    def get_violation(self, message: str) -> str:
        pass


class Student(Staff):
    def __init__(self, _personal_info: PersonalInfo, year: int, student_id: int, lessons_amount: int) -> None:
        super().__init__(_personal_info=_personal_info)
        self.id = student_id
        self.average_mark = 0.0
        self.year = year
        self.violations = list()
        self.enrollments = list()
        self.lessons_amount = lessons_amount

    def get_violation(self, message: str) -> str:
        self.violations.append(message)
        return message

    def calculate_workload(self) -> float:
        return self.lessons_amount * 2.5

    def visit_seminar(self, seminar: Seminar) -> None:
        pass

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
        self.enrollments[idx].course. \
            remove_student(student_id=self.id)
        del self.enrollments[idx]

    def can_enroll(self, course: Course) -> bool:
        if self.average_mark >= 4.5:
            return True

    def __str__(self):
        return f"Name: {self._personal_info.name}" \
               f"Address: {self._personal_info.address}" \
               f"Phone number: {self._personal_info.phone_number}" \
               f"Email: {self._personal_info.email}" \
               f"Position: {self._personal_info.position}" \
               f"Employed year: {self.year}"


class PostgraduateStudent(Staff):
    def __init__(self, _personal_info: PersonalInfo, phd_status: str, lessons_amount: int) -> None:
        super().__init__(_personal_info=_personal_info)
        self.phd_status = phd_status
        self.lessons_amount = lessons_amount

    def calculate_workload(self) -> float:
        return self.lessons_amount * 2.5

    def get_violation(self, message: str) -> str:
        pass

    def can_enroll(self, course: Course) -> bool:
        if self.lessons_amount < 5:
            return True

    def __str__(self):
        return f"ID: {self._personal_info.id}" \
               f"Name: {self._personal_info.name}" \
               f"Address: {self._personal_info.address}" \
               f"Phone number: {self._personal_info.phone_number}" \
               f"Email: {self._personal_info.email}" \
               f"Position: {self._personal_info.position}" \
               f"Employed year: {self._personal_info.employed_year}" \
               f"Status: {self.phd_status}"


class Professor(Staff):
    def __init__(self, _personal_info: PersonalInfo, salary: float, lessons_amount: int) -> None:
        super().__init__(_personal_info=_personal_info)
        self.salary = salary
        self.subordinate = []
        self.lessons_amount = lessons_amount

    def add_postgraduate_student(self) -> None:
        pass

    def get_violation(self, message: str) -> str:
        pass

    def calculate_workload(self) -> float:
        return self.lessons_amount * 1.5

    def can_enroll(self, course: Course) -> None:
        pass

    def __str__(self):
        return f"ID: {self._personal_info.id}" \
               f"Name: {self._personal_info.name}" \
               f"Address: {self._personal_info.address}" \
               f"Phone number: {self._personal_info.phone_number}" \
               f"Email: {self._personal_info.email}" \
               f"Position: {self._personal_info.position}" \
               f"Employed year: {self._personal_info.employed_year}" \
               f"Salary: {self.salary}"
