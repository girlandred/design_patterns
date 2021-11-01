from abc import abstractmethod, ABC
from datetime import datetime

from courses import Calculus, DesignPatterns, MachineLearning
from staff import Professor
from lab_3.group import Group
from personalInfo import PersonalInfo


class Administration(ABC):
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

    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        self._personal_info = personal_info
        self.group_id = group_id
        self.group_list = []
        self.course_list = []

    @abstractmethod
    def attach_course(self, *args):
        pass

    def fill_course(self, professor: Professor, group: Group) -> None:
        self.attach_course(professor, group)
        pass


class HeadDepartment(Administration):
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

    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        super().__init__(personal_info, group_id)

    def attach_course(self, *args):
        course2 = MachineLearning(id_=131, title='Machine Learning', fee=1240,
                                  starting_date=datetime(2002, 12, 1), seminars_number=12)
        course1 = DesignPatterns(id_=101, title='Design Patterns', fee=2500,
                                 starting_date=datetime(2002, 12, 1), seminars_number=44)
        return [course1, course2]


class Dean(Administration):
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

    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        super().__init__(personal_info, group_id)

    def attach_course(self, *args):
        course = Calculus(id_=1, title='Calculus', fee=1700,
                          starting_date=datetime(2021, 10, 29), seminars_number=32)
        return [course]
