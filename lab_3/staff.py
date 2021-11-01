from abc import abstractmethod, ABC
from typing import List

from lab_3.courses import Course
from lab_3.personalInfo import PersonalInfo


class Staff(ABC):
    """
        Represents staff.

        ...

        Attributes:
        ----------
        personal_info : PersonalInfo


        Methods:
        --------

        taken_seminars()
            Contain information about taken course.
        can_enroll(seminar: Course)
            Define if person can enroll in course.
        @abstractmethod
        calculate_workload()
            Method which calculating workload
        @abstractmethod
        get_violation()
            Method which showing violation
    """

    def __init__(self, personal_info: PersonalInfo) -> None:
        self.enrollments = list()
        self.comments = None
        self._personal_info = personal_info

    @property
    def personal_info(self) -> PersonalInfo:
        return self._personal_info

    @personal_info.setter
    def personal_info(self, _personal_info: PersonalInfo) -> None:
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


class Professor(Staff):
    """"
    Contain information about professor

    ...

    Attributes:
    ----------
        ...
        salary : float
            professor's salary
    Methods:
    --------
        calculate_workload()
            Method which calculating workload
        add_postgraduate_student
        get_violation(message: str)
        request_support()

    """

    def __init__(self, personal_info: PersonalInfo, salary: float, lessons_amount: int) -> None:
        super().__init__(personal_info=personal_info)
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
        return print(f"ID: {self._personal_info.id} \n"
                     f"Name: {self._personal_info.name} \n"
                     f"Address: {self._personal_info.address} \n"
                     f"Phone number: {self._personal_info.phone_number} \n"
                     f"Email: {self._personal_info.email} \n"
                     f"Position: {self._personal_info.position} \n"
                     f"Employed year: {self._personal_info.employed_year} \n"
                     f"Salary: {self.salary}")
