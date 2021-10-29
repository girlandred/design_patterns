from abc import abstractmethod, ABC
from personalInfo import PersonalInfo


class Administration(ABC):
    def __init__(self, personal_info: PersonalInfo, group_id: int) -> None:
        self._personal_info = personal_info
        self.group_id = group_id
        self.group_list = []

    @abstractmethod
    def attach_course(self, *args):
        pass

    def fill_course(self, groups) -> None:
        self.group_list.append(self.group_id)
        return print(f"For group {self.group_id} was added courses")


class HeadDepartment(Administration):
    def attach_course(*args):
        pass


class Dean(Administration):
    def attach_course(self, *args):
        pass
