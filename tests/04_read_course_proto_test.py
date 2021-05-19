"""Test read_course_proto.

This module tests the correctness and exceptions of ReadCourseData/read_course_proto()
"""


import sys
sys.path.append('./src')
from ReadCourseData import read_course_proto
from InsertData import check_file_open
import pytest
import targetOutput as target_output

def test_read_course_proto_correctness():
    """Test if read_course_proto() returns the right content with/without lab."""
    course_raw_data = check_file_open('tests/test.json')
    json_obj = course_raw_data['Test Data']
    course_list = []
    enrollment_dict = {}
    index = 0
    department_name = 'ACCT'
    each_department = read_course_proto(json_obj, course_list, department_name, enrollment_dict)
    assert each_department.deptName == 'ACCT'
    assert len(each_department.courses) == 3
    assert len(course_list) == 3
    for i in range(len(each_department.courses)):
        assert each_department.courses[i] == target_output.department_acct.courses[i]
    for i in range(len(course_list)):
        assert course_list[i] == target_output.courseList[i]
    for key in enrollment_dict.keys():
        assert enrollment_dict[key] == target_output.seats[index]
        index += 1
    
    course_list = []
    department_name = 'ADMJ'
    enrollment_dict = {}
    each_department = read_course_proto(json_obj, course_list, department_name, enrollment_dict)
    assert each_department.deptName == 'ADMJ'
    assert len(each_department.courses) == 3
    assert len(course_list) == 3
    for i in range(len(each_department.courses)):
        assert each_department.courses[i] == target_output.department_admj.courses[i]
    for i in range(len(course_list)):
        assert course_list[i] == target_output.courseList[i + 3]
    for key in enrollment_dict.keys():
        assert enrollment_dict[key] == target_output.seats[index]
        index += 1
