"""Test inser_data.

This module tests the correctness and exceptions of InsertData/inser_data()
"""


import sys
sys.path.append('./src')
from pathlib import Path
from InsertData import check_file_open, insert_data, get_db
from ReadCourseData import from_raw_to_list
from dotenv import load_dotenv

load_dotenv()

def test_insert_data_correctness():
    """Test if insert_data() returns the right content."""
    course_raw_data = check_file_open('tests/test.json')
    course_list, department_list = from_raw_to_list(course_raw_data, 'Test Data')
    insert_data(course_list, department_list, 'Test Data')
    db = get_db()
    assert (db['Test Data courses'].find_one({'crn': '32072'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '35071'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '31138'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '00053'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '00054'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '35528'})) is not None
    assert (db['Test Data departments'].find_one({'deptName': 'ACCT'})) is not None
    assert (db['Test Data departments'].find_one({'deptName': 'ADMJ'})) is not None
    assert len(db['Test Data departments'].find_one({'deptName': 'ACCT'})['courses']) == 3
    assert len(db['Test Data departments'].find_one({'deptName': 'ADMJ'})['courses']) == 3
