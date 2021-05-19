# -*- coding: utf-8 -*-
"""Insert Data component.

This module gets lists of Course and Department objects from ReadCourseData.py
and inserts those data into the desired database
"""


import os, json, letslog
from google.protobuf.json_format import MessageToDict
from ReadCourseData import from_raw_to_list
from pymongo import MongoClient, errors as mongoerrors
from pathlib import Path
from dotenv import load_dotenv

##read env variable
load_dotenv()
logger = letslog.Letslog(os.path.dirname(os.path.abspath(__file__))+'/../log')
logger.initiateLogger("_InsertData", "INFO")

QUARTER_INDEX = -16
ACTIVE = 'Act'
REMAIN = 'Rem'
WAITLIST_REMAIN = 'WL Rem'

def get_db():
    """Get MongoDB username and password from the env variables and return the desired database.

    Raises:
        pymongo.errors: possibly connection errors or conficuration errors
    Returns:
        The database object

    """
    username, password = os.getenv('Mongo_User'), os.getenv('Mongo_Password')
    db_name = os.getenv('Mongo_DBName')
    client = MongoClient('mongodb+srv://' + username + ':' + password
                         + os.getenv('Mongo_Postfix'))
    return client.get_database(db_name)


def check_file_open(filename):
    """Check if the json file exists in the specified directory.

    Args:
        filename: the path to the desired file
    Raises:
        FileNotFoundError: File does not exit
    Returns:
        The database object

    """
    if filename:
        with open(filename, 'r') as file:
            return json.load(file)
    raise FileNotFoundError('File {filename} is not found!')


def insert_data(course_list, dept_list, enrollment_dict, quarter_name):
    """Insert data into database.

    Get every single Course and Department object from the lists and
    insert them into the correct database collections
        (named quarter_name + 'course'/'departments')

    Args:
        course_list: the list of Course objects
        dept_list: the list of Department objects
        quarter_name: str, the name of the quarter
    Raises:
        pymongo.errors: possibly connection errors or configuration errors
    Returns:
        None

    """
    database = get_db()
    course_collection = database[quarter_name + ' courses']
    dept_collection = database[quarter_name + ' departments']
    seat_collection = database[quarter_name + ' seats']
    
    for course in course_list:
        temp_course = MessageToDict(course)
        course_collection.replace_one({'crn': temp_course['crn']}, temp_course, upsert=True)
    for dept in dept_list:
        temp_dept = MessageToDict(dept)
        dept_collection.replace_one({'deptName': temp_dept['deptName']}, temp_dept, upsert=True)
    inserted_seats = seat_collection.find()
    if (quarter_name + ' seats') not in database.list_collection_names() or inserted_seats.count() == 0:
        for crn in enrollment_dict.keys():
            inserted_seat = {'UID': crn, 'latest': enrollment_dict[crn]['fetch_time_datetime'],
                'fetch_time_datetime': [enrollment_dict[crn]['fetch_time_datetime']],
                'fetch_time': [enrollment_dict[crn]['fetch_time']], ACTIVE: [enrollment_dict[crn][ACTIVE]],
                REMAIN: [enrollment_dict[crn][REMAIN]], WAITLIST_REMAIN: [enrollment_dict[crn][WAITLIST_REMAIN]]}
            seat_collection.insert_one(inserted_seat)
    else:
        for inserted_seat in inserted_seats:
            update_seat = inserted_seat
            crn = inserted_seat['UID']
            if enrollment_dict[crn]['fetch_time_datetime'] > update_seat['latest']:
                update_seat['fetch_time_datetime'].append(enrollment_dict[crn]['fetch_time_datetime'])
                update_seat['fetch_time'].append(enrollment_dict[crn]['fetch_time'])
                update_seat[ACTIVE].append(enrollment_dict[crn][ACTIVE])
                update_seat[REMAIN].append(enrollment_dict[crn][REMAIN])
                update_seat[WAITLIST_REMAIN].append(enrollment_dict[crn][WAITLIST_REMAIN])
                update_seat['latest'] = enrollment_dict[crn]['fetch_time_datetime']
                seat_collection.replace_one({'UID': crn}, update_seat)


def main():
    """Runner of this DBImport program.

    With the help of other functions, this main function could read the data from
    JSON files and put them into desired databases.
    """
    try:
        print("start upload...")
        logger.log('InsertData.py Excecution Started.')
        path = os.getenv('data_path')
        year = int(os.getenv('start_year'))
        while os.getenv(str(year)):
            all_quarters_in_year = os.getenv(str(year)).split(',')
            for each_quarter in all_quarters_in_year:
                quarter_name = each_quarter[:QUARTER_INDEX].replace('_', ' ')
                filename = path + each_quarter
                course_raw_data = check_file_open(filename)
                course_list, department_list, enrollment_dict = from_raw_to_list(course_raw_data, quarter_name)
                insert_data(course_list, department_list, enrollment_dict, quarter_name)
            year += 1
    except mongoerrors.PyMongoError:
        logger.error('MongoDB error has occurred')
    except (FileNotFoundError, KeyError) as err:
        logger.error(err)
    finally:
        logger.log('InsertData.py Excecution Finished.')


if __name__ == "__main__":
    main()
