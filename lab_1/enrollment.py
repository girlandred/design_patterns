from lab_1.course import Course
from datetime import datetime


class Enrollment:
    def __init__(self, course: Course):
        self.received_marks = dict()
        self.course = course

    def get_average_to_date(self, date_to: datetime) -> float:
        grades = []
        for date, grade in self.received_marks.items():
            if date <= date_to:
                grades.append(grade)

        return sum(grades)/len(grades)

    def get_final_mark(self) -> float:
        total_sum = float(sum(self.received_marks.values()))
        return total_sum / len(self.received_marks)

    def __str__(self):
        return f"Received marks are {self.received_marks}"
