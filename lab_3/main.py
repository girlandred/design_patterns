from __future__ import annotations

from datetime import datetime

import courses
from group import Group


course1 = courses.MachineLearning(id_=131, title='Machine Learning', fee=1240,
                                  starting_date=datetime(2002, 12, 1), seminars_number=12)
group1 = Group(12, 'Machine Learning', 24)
course1.add_group(group1.group_id)
course1.send_course_materials(group=group1)
course1.remove_group(group1.group_id)
group1.__repr__()

course = courses.DesignPatterns(id_=101, title='Design Patterns', fee=2500,
                                starting_date=datetime(2002, 12, 1), seminars_number=44)
group2 = Group(32, 'Design Patterns', 24)
course.add_group(group2.group_id)
course.send_course_materials(group=group2)
course.remove_group(group2.group_id)
group2.__repr__()
