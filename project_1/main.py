from datetime import datetime

from project_1.course import Course, CourseInformation
from staff import Professor, Student


course_info = CourseInformation(id_=1, title='math',
                                starting_date=datetime.now(),
                                seminars_number=14, fee=100.05)

course = Course(course_info=course_info)
professor = Professor(name='test pf', phone_number='111', address='test pf',
                      salary=10000, email='test_pf@test.test', course=course)
student = Student(id_=1, name='test', address='somewhere there',
                  phone_number='911', email='test@test.test',
                  student_number=1)
student.enroll(course=course)
