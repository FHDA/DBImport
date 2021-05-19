"""Test from_raw_to_list.

This module tests the correctness and exceptions of ReadCourseData/from_raw_to_list()
"""


import sys
sys.path.append('./src')
from ReadCourseData import from_raw_to_list
from InsertData import check_file_open
import pytest
import targetOutput as target_output

def test_from_raw_to_list_correctness():
    """Test if from_raw_to_list() returns the right content."""
    course_raw = check_file_open('tests/test.json')
    index = 0
    quarter_name = 'Test Data'
    course_list, department_list, enrollment_dict = from_raw_to_list(course_raw, quarter_name)
    assert len(course_list) == 6
    assert len(department_list) == 2
    for i in range(len(course_list)):
        assert course_list[i] == target_output.courseList[i]
    for i in range(len(department_list)):
        for j in range(3):
            assert department_list[i].courses[j] == target_output.departmentList[i].courses[j]
    for key in enrollment_dict.keys():
        assert enrollment_dict[key] == target_output.seats[index]
        index += 1


def test_from_raw_to_list_with_invalid_quarter_name():
    """Test if from_raw_to_list() throws the right exception if the quarter name is invalid."""
    with pytest.raises(KeyError):
        course_raw = check_file_open('tests/test.json')
        quarter_name = 'Invalid quarter name'
        course_list, department_list, enrollment_dict = from_raw_to_list(course_raw, quarter_name)


def test_from_raw_to_list_with_invalid_file():
    """Test if from_raw_to_list() throws the right exception if the json file is invalid."""
    with pytest.raises(FileNotFoundError):
        course_raw = check_file_open('tests/nonexistent.json')
        quarter_name = 'Test Data'
        course_list, department_list, enrollment_dict = from_raw_to_list(course_raw, quarter_name)

