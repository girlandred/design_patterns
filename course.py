import datetime


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
