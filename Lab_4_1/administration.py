from abc import ABC, abstractmethod

from Lab_4_1.course import Seminar, Course
from Lab_4_1.personalInfo import PersonalInfo
from Lab_4_1.staff import Student, Professor


class Manager(ABC):

    @abstractmethod
    def attach_students(self, *args):
        pass

    @abstractmethod
    def set_course_date(self):
        pass

    @abstractmethod
    def set_name(self):
        pass


class Dean(Manager):
    """
        Represents Dean course.

        ...

        Attributes:
        ----------
            group_id : int
                Contain information about groups id

        Methods:
        --------
            attach_course()
                Attaching course to head department
        """

    def __init__(self, personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)

    def attach_students(self, *args):
        student = Student()
        return [student]

    def set_course_date(self):
        date = None
        pass

    def set_name(self):
        name = None
        pass

    def create_seminars(self, *args):
        seminar = Seminar()
        professor = Professor()
        return self.create_seminars(seminar, professor)


class HeadDepartment(Manager):
    """
        Represents HeadDepartment course.

        ...

        Attributes:
        ----------
            group_id : int
                contain information about groups id

        Methods:
        --------
            attach_course()
                Attaching course to head department
        """

    def attach_students(*args):
        student = Student()
        return [student]

    def set_course_date(self):
        date = None
        pass

    def set_name(self):
        name = None
        pass

    def create_course(self, *args):
        course = Course()
        professor = Professor()
        return self.create_course(course, professor)


class Administration(ABC):
    """
        Represents Administration class.

        ...
        Methods:
        --------
            attach_course()

            fill_course()

        """

    __manager = None

    def set_manager(self, manager):
        self.__manager = manager

    def fill_course(self, professor: Professor, student: Student, course: Course):
        return self.fill_course(professor, student, course)
