"""Test read_lab_time.

This module tests the correctness and exceptions of ReadCourseData/read_lab_time()
"""

import sys
sys.path.append('./src')
from InsertData import check_file_open
from ReadCourseData import read_lab_time
import course_pb2 as course
import targetOutput as target_output

def test_read_lab_time_correctness_lab():
    """Test if read_lab_time() returns the right content if the course has a lab."""
    file_obj = check_file_open('tests/test_lab.json')
    each_courses = file_obj['Test Data']['CourseData']['ACCT']
    for i in range(len(each_courses)):
        each_course = each_courses[i]
        temp_course = course.Course()
        temp_course = read_lab_time(each_course, temp_course)
        assert temp_course == target_output.labs[i]


def test_read_lab_time_correctness_nolab():
    """Test if read_lab_time() returns the right content if the course has no lab."""
    file_obj = check_file_open('tests/test_lab.json')
    each_course = file_obj['Test Data']['CourseData']['ACCT'][2]
    temp_course = course.Course()
    temp_course = read_lab_time(each_course, temp_course)
    assert len(temp_course.lab) == 0
