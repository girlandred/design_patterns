from __future__ import annotations
from datetime import datetime
from group import Group
import courses

course1 = courses.MachineLearning(id_=1, title='Machine Learning', fee=12400,
                                  starting_date=datetime(2002, 12, 1), seminars_number=32)
group1 = Group(12, 'Machine Learning', 24)
course1.add_group(group1.group_id)
course1.send_course_materials(group=group1)
course1.remove_group(group1.group_id)
group1.__repr__()

course = courses.DesignPatterns(id_=1, title='Design Patterns', fee=12400,
                                starting_date=datetime(2002, 12, 1), seminars_number=32)
group2 = Group(32, 'Design Patterns', 24)
course.add_group(group2.group_id)
course.send_course_materials(group=group2)
course.remove_group(group2.group_id)
group2.__repr__()
