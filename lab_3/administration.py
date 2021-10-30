from abc import abstractmethod, ABC
from datetime import datetime

from courses import Calculus, DesignPatterns, MachineLearning
from personalInfo import PersonalInfo

"""
    Represents Administration class.

    ...

    Attributes:
    ----------
        group_id : int
            contain information about groups id


    Methods:
    --------
        attach_course()
            
        fill_course()
            
    """


class Administration(ABC):
    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        self._personal_info = personal_info
        self.group_id = group_id
        self.group_list = []
        self.course_list = []

    @abstractmethod
    def attach_course(self, *args):
        pass

    def fill_course(self, groups) -> None:
        self.group_list.append(self.group_id)
        return print(f"For group {self.group_id} was added courses")


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


class HeadDepartment(Administration):
    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        super().__init__(personal_info, group_id)
        self.course2 = MachineLearning(id_=131, title='Machine Learning', fee=1240,
                                       starting_date=datetime(2002, 12, 1), seminars_number=12)
        self.course1 = DesignPatterns(id_=101, title='Design Patterns', fee=2500,
                                      starting_date=datetime(2002, 12, 1), seminars_number=44)

    def attach_course(self, *args):
        print("Which course you would like to attach?")
        choice = input()
        if choice == '1':
            self.course_list.append(self.course1)
            return print(f"Head Department was attached to course. {self.course1}")
        if choice == '2':
            self.course_list.append(self.course2)
            return print(f"Head Department was attached to course. {self.course2}")
        else:
            return print("Wrong input")


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


class Dean(Administration):
    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        super().__init__(personal_info, group_id)
        self.course = Calculus(id_=1, title='Calculus', fee=1700,
                               starting_date=datetime(2021, 10, 29), seminars_number=32)
        self.course_list = []

    def attach_course(self, *args):
        self.course_list.append(self.course)
        return print(f"Dean was attached to course. {self.course}")
