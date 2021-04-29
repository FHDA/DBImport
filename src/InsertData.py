# -*- coding: utf-8 -*-
"""Insert Data component.

This module gets lists of Course and Department objects from ReadCourseData.py
and inserts those data into the desired database
"""

import json, os, sys, letslog
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\pb2')
from google.protobuf.json_format import MessageToDict
from ReadCourseData import from_raw_to_list
from configparser import ConfigParser
from pymongo import MongoClient
from pymongo import errors as mongoerrors

logger = letslog.Letslog(os.path.dirname(os.path.abspath(__file__))+'\\..\\log')
logger.initiateLogger("_InsertData", "INFO")
env_config = ConfigParser()
env_config.read(os.path.dirname(os.path.abspath(__file__))+'\\..\\config\\setting.config')
mongo_config = env_config['MongoDB']
QUARTER_INDEX = -16

def get_db():
    """Get MongoDB username and password from the config file and return the desired database.

    Raises:
        pymongo.errors: possibly connection errors or conficuration errors
    Returns:
        The database object

    """
    username, password = mongo_config['Mongo_User'], mongo_config['Mongo_Password']
    db_name = mongo_config['Mongo_DBName']
    client = MongoClient('mongodb+srv://' + username + ':' + password
                         + mongo_config['Mongo_Postfix'])
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


def insert_data(course_list, dept_list, seat_dict, quarter_name):
    """Insert data into database.

    Get every single Course and Department object from the lists and
    insert them into the correct database collections
        (named quarter_name + 'course'/'departments')

    Args:
        course_list: the list of Course objects
        dept_list: the list of Department objects
        seat_list: the dictionary of enrollment data
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

    # for course in course_list:
    #     temp_course = MessageToDict(course)
    #     course_collection.update(temp_course, temp_course, upsert=True)
    # for dept in dept_list:
    #     temp_dept = MessageToDict(dept)
    #     dept_collection.update(temp_dept, temp_dept, upsert=True)
    for crn in seat_dict.keys():
        inserted_seat = seat_collection.find_one({"UID": crn})
        if not inserted_seat:
            inserted_seat = {"UID": crn, crn: [seat_dict[crn]], 'latest': seat_dict[crn]['fetch_time_datetime']}
            seat_collection.replace_one({'UID': crn}, inserted_seat, upsert=True)
        else:
            if seat_dict[crn]['fetch_time_datetime'] > inserted_seat['latest']:
                inserted_seat[crn].append(seat_dict[crn])
                inserted_seat['latest'] = seat_dict[crn]['fetch_time_datetime']
                seat_collection.replace_one({'UID': crn}, inserted_seat, upsert=True)


def main():
    """Runner of this DBImport program.

    With the help of other functions, this main function could read the data from
    JSON files and put them into desired databases.
    """
    logger.log('InsertData.py Excecution Started.')
    config = ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__))+'\\..\\config\\'+env_config['Config']['Config_File_Name'])
    logger.log('Config read completed.')
    path = config['locations']['path']
    logger.log('Processing data files located in: ' + path)
    year = int(config['data_info']['start_year'])

    try:
        while config['locations'][str(year)]:
            all_quarters_in_year = config['locations'][str(year)].split(',')
            for each_quarter in all_quarters_in_year:
                quarter_name = each_quarter[:QUARTER_INDEX].replace('_', ' ')
                logger.log('Inserting %s' % quarter_name)
                filename = path + each_quarter
                logger.log(filename)
                course_raw_data = check_file_open(filename)
                course_list, department_list, seat_dict = from_raw_to_list(course_raw_data, quarter_name)
                insert_data(course_list, department_list, seat_dict, quarter_name)
                logger.log('Inserted %s' % quarter_name)
            year += 1
    except mongoerrors.PyMongoError as err:
        logger.error(f'MongoDB error has occurred: {err}')
    except (FileNotFoundError, KeyError) as err:
        logger.error(err)
    logger.log('InsertData.py Excecution Finished.')


if __name__ == "__main__":
    main()
