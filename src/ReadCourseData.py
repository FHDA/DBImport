# -*- coding: utf-8 -*-
"""Read Course Data component.

This module helps the runner to read course data from json files and return
lists of Course and Department objects for databse insertion
"""

import json, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/pb2')
import course_pb2 as course
import instructor_pb2 as instructor
import department_pb2 as department
from pymongo import MongoClient
from pathlib import Path

def read_course_proto(json_object, course_list, department_name):
    """Convert course json object to lists of objects, using Protocol Buffer generated class

    With the raw json file of the quarter,
    and the department name, this function reads data from json file and initializes Course objects
    using the data from json file. The initialized Course objects will be put into the course_list
    argument and the list of all course titles under this department name will be returned

    Args:
      json_object: the list which generated by reading the json file

      course_list: the list of courses, mutates during runtime to
                          be filled with course objects
      department_name: the department name, used to access the json file
                      and to record what courses are in this department
    Raises:
        KeyError: If the attributes provided are not in the json key list
    Returns:
        The list containing the name of all courses in this department

    """
    each_department = department.Department()
    each_department.deptName = department_name
    for each_course in json_object['CourseData'][department_name]:
        temp_course = course.Course()
        temp_course.UID = each_course['CRN']
        temp_course.crn = each_course['CRN']
        temp_course.course_num = each_course['Crse']
        temp_course.section_num = each_course['Sec']
        temp_course.campus = each_course['Cmp']
        temp_course.num_credit = float(each_course['Cred'])
        temp_course.course_title = each_course['Title']
        temp_course.startTime = each_course['Time'][:8]
        temp_course.endTime = each_course['Time'][9:]
        temp_course.cap = int(each_course['Act']) + int(each_course['Rem'])
        temp_course.instructor_name = each_course['Instructor']
        temp_course.startDate = each_course['Date (MM/DD)'][:5]
        temp_course.endDate = each_course['Date (MM/DD)'][6:]
        temp_course.location = each_course['Location']
        temp_course.days = 'ONLINE' if ('ONLINE' in temp_course.location) else each_course['Days']
        temp_course.attribute = each_course['Attribute']
        temp_course = read_lab_time(each_course, temp_course)
        course_list.append(temp_course)
        if temp_course not in each_department.courses:
            each_department.courses.append(temp_course)
    return each_department


def read_lab_time(each_course, temp_course):
    """Read lab info if a lab exists in the course.

    Args:
        each_course: the course to be checked if lab exist
        temp_course: the course object to be added to the database
    Raises:
        KeyError: If the 'course_raw' attribute provided is not in the json key list
    Returns:
        the course object with its lab session

    """
    if each_course['lab']:
        temp_lab = temp_course.lab.add()
        temp_lab.UID = temp_course.UID + 'L'
        lab_info = each_course['lab'][0]
        temp_lab.days = '' if 'Days' not in lab_info else lab_info['Days']
        temp_lab.time = lab_info['Time']
        temp_lab.startDate = lab_info['Date (MM/DD)'][:5]
        temp_lab.endDate = lab_info['Date (MM/DD)'][6:]
        temp_lab.instructor = lab_info['Instructor']
        temp_lab.location = lab_info['Location']
    return temp_course


def from_raw_to_list(course_raw, quarter_name):
    """Convert opened json files to two lists of Course objects and Department objects.

    Args:
        course_raw: opened json file
        quarter_name: the name of the quarter, used to access the 'CourseData' key in the json file
    Raises:
        KeyError: If the 'course_raw' attribute provided is not in the json key list
    Returns:
        the two lists of Course objects and Department objects

    """
    course_list, department_list = [], []
    for department_name in course_raw[quarter_name]['CourseData']:
        department_list.append(read_course_proto(course_raw[quarter_name],
                                                 course_list, department_name))
    return course_list, department_list
