import datetime

from course1 import CourseInformation, Course
from personalInfo import PersonalInfo
from staff1 import Student, PostgraduateStudent, Professor

course_info = CourseInformation('math', datetime.datetime(2001, 12, 3), 3, 34.000)
course = Course(1, course_info)

student_info = PersonalInfo(1, 'Maryna', 'Kiev', '09445', 'test@test.gmail.com',
                            'Sophomore', datetime.datetime(2001, 12, 3),)
maryna = Student(student_info, 2, 4, 3)
maryna.__str__()

ps_info = PersonalInfo(12, 'Ihor', 'Kharkov', '03032', 'mailtest@gmail.com',
                       'postgraduate student', datetime.datetime(2001, 12, 3))
ihor = PostgraduateStudent(ps_info, 'junior', 2)
info = ihor.__str__

professor_info = PersonalInfo(32, 'David', 'Lvov', '7437872', 'sjfhsjj@gmail.com',
                              'docent', datetime.datetime(2001, 12, 3),)
david = Professor(professor_info, 10.0, 4)
