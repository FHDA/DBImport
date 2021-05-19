import sys
sys.path.append('./src')
import course_pb2 as course
import department_pb2 as department

courseList = []
departmentList = []
labs = []

course_32072 = course.Course()
course_32072.UID = '32072'
course_32072.crn = '32072'
course_32072.course_num = 'D001A'
course_32072.section_num = '12'
course_32072.campus = 'DA'
course_32072.num_credit = 5.000
course_32072.course_title = 'FINAN ACCOUNTNG I'
course_32072.days = 'TR'
course_32072.startTime = '11:00 am'
course_32072.endTime = '01:15 pm'
course_32072.cap = 45
course_32072.instructor_name = 'Mary,Amelia,Breen'
course_32072.startDate = '01/08'
course_32072.endDate = '03/30'
course_32072.location = 'DA L84'
course_32072.attribute = ''

course_35071 = course.Course()
course_35071.UID = '35071'
course_35071.crn = '35071'
course_35071.course_num = 'D074'
course_35071.section_num = '01'
course_35071.campus = 'DA'
course_35071.num_credit = 5.000
course_35071.course_title = 'ACCOUNTING ETHICS'
course_35071.days = 'ONLINE'
course_35071.startTime = 'TBA'
course_35071.endTime = ''
course_35071.cap = 45
course_35071.instructor_name = 'Walter,Michael,Gough'
course_35071.startDate = '01/08'
course_35071.endDate = '03/30'
course_35071.location = 'DA ONLINE'
course_35071.attribute = ''
lab = course_35071.lab.add()
lab.UID = '35071L'
lab.days = ''
lab.time = 'TBA'
lab.startDate = '06/28'
lab.endDate = '08/07'
lab.instructor = 'Christopher,C,Kwak'
lab.location = 'DA LC107'

course_31138 = course.Course()
course_31138.UID = '31138'
course_31138.crn = '31138'
course_31138.course_num = 'D105'
course_31138.section_num = '01'
course_31138.campus = 'DA'
course_31138.num_credit = 1.000
course_31138.course_title = 'BASIC FINANCIAL ACCT PROCEDURE'
course_31138.days = 'T'
course_31138.startTime = '05:00 pm'
course_31138.endTime = '05:50 pm'
course_31138.cap = 22
course_31138.instructor_name = 'Laurienne,Bermudez,Hammond'
course_31138.startDate = '01/08'
course_31138.endDate = '03/30'
course_31138.location = 'DA AT202'
course_31138.attribute = ''

course_00053 = course.Course()
course_00053.UID = '00053'
course_00053.crn = '00053'
course_00053.course_num = 'D001'
course_00053.section_num = '01'
course_00053.campus = 'DA'
course_00053.num_credit = 4.000
course_00053.course_title = 'INTRO TO ADMIN OF JUSTICE'
course_00053.days = 'MTWR'
course_00053.startTime = '08:30 am'
course_00053.endTime = '09:20 am'
course_00053.cap = 46
course_00053.instructor_name = 'Marni,Kristine,Lawlor'
course_00053.startDate = '01/08'
course_00053.endDate = '03/30'
course_00053.location = 'DA L22'
course_00053.attribute = ''

course_00054 = course.Course()
course_00054.UID = '00054'
course_00054.crn = '00054'
course_00054.course_num = 'D003'
course_00054.section_num = '01'
course_00054.campus = 'DA'
course_00054.num_credit = 4.000
course_00054.course_title = 'CONCEPTS OF CRIM LAW (CP 2)'
course_00054.days = 'MTWR'
course_00054.startTime = '09:30 am'
course_00054.endTime = '10:20 am'
course_00054.cap = 34
course_00054.instructor_name = 'Terry,R,Ellis'
course_00054.startDate = '01/08'
course_00054.endDate = '03/30'
course_00054.location = 'DA L22'
course_00054.attribute = ''

course_35528 = course.Course()
course_35528.UID = '35528'
course_35528.crn = '35528'
course_35528.course_num = 'D064Y'
course_35528.section_num = '56'
course_35528.campus = 'DA'
course_35528.num_credit = 3.000
course_35528.course_title = 'ADMJ INTRNSHIP'
course_35528.days = 'MWF'
course_35528.startTime = '12:30 pm'
course_35528.endTime = '03:20 pm'
course_35528.cap = 5
course_35528.instructor_name = 'Terry,R,Ellis'
course_35528.startDate = '01/08'
course_35528.endDate = '03/30'
course_35528.location = 'DA L13C'
course_35528.attribute = ''

courseList.append(course_32072)
courseList.append(course_35071)
courseList.append(course_31138)
courseList.append(course_00053)
courseList.append(course_00054)
courseList.append(course_35528)

department_acct = department.Department()
department_acct.deptName = 'ACCT'
department_acct.courses.append(course_32072)
department_acct.courses.append(course_35071)
department_acct.courses.append(course_31138)

department_admj = department.Department()
department_admj.deptName = 'ADMJ'
department_admj.courses.append(course_00053)
department_admj.courses.append(course_00054)
department_admj.courses.append(course_35528)

departmentList.append(department_acct)
departmentList.append(department_admj)

lab_35071 = course.Course()
lab = lab_35071.lab.add()
lab.UID = 'L'
lab.days = ''
lab.time = 'TBA'
lab.startDate = '06/28'
lab.endDate = '08/07'
lab.instructor = 'Christopher,C,Kwak'
lab.location = 'DA LC107'

lab_00007 = course.Course()
lab = lab_00007.lab.add()
lab.UID = 'L'
lab.days = ''
lab.time = 'TBA'
lab.startDate = '06/28'
lab.endDate = '08/07'
lab.instructor = 'Walter,Michael,Gough'
lab.location = 'DA LC107'

lab_00011 = course.Course()

labs.append(lab_35071)
labs.append(lab_00007)
labs.append(lab_00011)

seats = []
secondTimeSeats = []

seat1 = {
    'crn': '32072',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 40,
    'Rem': 5,
    'WL Rem': 5
}

seat2 = {
    'crn': '35071',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 40,
    'Rem': 5,
    'WL Rem': 5
}

seat3 = {
    'crn': '31138',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 17,
    'Rem': 5,
    'WL Rem': 5
}

seat4 = {
    'crn': '00053',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 41,
    'Rem': 5,
    'WL Rem': 15
}

seat5 = {
    'crn': '00054',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 29,
    'Rem': 5,
    'WL Rem': 15
}

seat6 = {
    'crn': '35528',
    'fetch_time_datetime': 1620739965,
    'fetch_time': '05/11/2021, 06:32:45',
    'Act': 0,
    'Rem': 5,
    'WL Rem': 0
}

seats.append(seat1)
seats.append(seat2)
seats.append(seat3)
seats.append(seat4)
seats.append(seat5)
seats.append(seat6)

seat1Second = {
    'UID': '32072',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [40, 40],
    'Rem': [5, 5],
    'WL Rem': [5, 5]
}

seat2Second = {
    'UID': '35071',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [40, 40],
    'Rem': [5, 5],
    'WL Rem': [5, 5]
}

seat3Second = {
    'UID': '31138',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [17, 17],
    'Rem': [5, 5],
    'WL Rem': [5, 5]
}

seat4Second = {
    'UID': '00053',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [41, 41],
    'Rem': [5, 5],
    'WL Rem': [15, 15]
}

seat5Second = {
    'UID': '00054',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [29, 29],
    'Rem': [5, 5],
    'WL Rem': [15, 15]
}

seat6Second = {
    'UID': '35528',
    'latest': 1620939965,
    'fetch_time_datetime': [1620739965, 1620939965],
    'fetch_time': ['05/11/2021, 06:32:45', '05/13/2021, 14:06:05'],
    'Act': [0, 0],
    'Rem': [5, 5],
    'WL Rem': [0, 0]
}

secondTimeSeats.append(seat1Second)
secondTimeSeats.append(seat2Second)
secondTimeSeats.append(seat3Second)
secondTimeSeats.append(seat4Second)
secondTimeSeats.append(seat5Second)
secondTimeSeats.append(seat6Second)
