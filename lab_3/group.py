class Group:
    """
        Represents groups

        ...

        Attributes:
        ----------
            group_id : int
                group's id.
            studying_course : str
                course which studying group.
            quantity_of_student : int
                information amount of student

        """

    def __init__(self, group_id: int, studying_course: str,
                 quantity_of_student: int):
        self.group_id = group_id
        self.studying_course = studying_course
        self.quantity_of_student = quantity_of_student

    def __repr__(self):
        print(f"Group id: {self.group_id}\n"
              f"Studying course: {self.studying_course}\n"
              f"Amount of students: {self.quantity_of_student}")
