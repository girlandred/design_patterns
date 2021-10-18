import datetime

from course import CourseInformation, Course
from personalInfo import PersonalInfo
from staff import Student, PostgraduateStudent, Professor

course_info = CourseInformation(title='Math', starting_date=datetime.datetime(2002, 12, 1),
                                seminars_number=3, fee=21333)
course = Course(course_info=course_info, _id=11)

student_info = PersonalInfo(id=1, name='Maryna', address='Kiev', email='someaddress@gmail.com',
                            phone_number='000000', position='Sophomore',
                            employed_year=datetime.datetime(2019, 8, 12))
maryna_student = Student(student_info, year=2019, student_id=12, lessons_amount=4)
maryna_student.__str__()

professor_info = PersonalInfo(id=1444, name='Ihor', address='Kharkov', phone_number='11111111',
                              email='email@gmail.com', position='Docent',
                              employed_year=datetime.datetime(1934, 12, 1))
professor = Professor(professor_info, lessons_amount=143, salary=10)
print('\t\n')
professor.__str__()

postgraduate_info = PersonalInfo(id=1232, name='Stepan', address='Zhmerynka', phone_number='12212112',
                                 email='postaddress@gmail.com', position='Postgraduate student',
                                 employed_year=datetime.datetime(2011, 4, 21))
postgraduate_student = PostgraduateStudent(postgraduate_info, lessons_amount=12, phd_status='None')


maryna_student.enroll(course)
