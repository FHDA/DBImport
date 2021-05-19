"""Test inser_data.
    
    This module tests the correctness and exceptions of InsertData/inser_data()
    """


import sys
sys.path.append('./src')
from pathlib import Path
from InsertData import check_file_open, insert_data, get_db
from ReadCourseData import from_raw_to_list
from dotenv import load_dotenv
import targetOutput as target_output

load_dotenv()

def test_multi_upload_correctness():
    """Test if insert_data() returns the right content."""
    course_raw_data = check_file_open('tests/test.json')
    course_list, department_list, enrollment_dict = from_raw_to_list(course_raw_data, 'Test Data')
    insert_data(course_list, department_list, enrollment_dict, 'Test Data')

    ##change time stamp
    course_raw_data['Test Data']['FetchTime'] = 1620939965
    course_list, department_list, enrollment_dict = from_raw_to_list(course_raw_data, 'Test Data')
    insert_data(course_list, department_list, enrollment_dict, 'Test Data')
    db = get_db()
    
    seat = db['Test Data seats'].find_one({'UID': '32072'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[0]
    
    seat = db['Test Data seats'].find_one({'UID': '35071'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[1]
    
    seat = db['Test Data seats'].find_one({'UID': '31138'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[2]
    
    seat = db['Test Data seats'].find_one({'UID': '00053'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[3]
    
    seat = db['Test Data seats'].find_one({'UID': '00054'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[4]
    
    seat = db['Test Data seats'].find_one({'UID': '35528'})
    del seat['_id']
    assert seat == target_output.secondTimeSeats[5]

    db['Test Data courses'].drop()
    db['Test Data departments'].drop()
    db['Test Data seats'].drop()

