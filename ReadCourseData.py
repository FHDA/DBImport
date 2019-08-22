import os, json
import os,inspect
from pymongo import MongoClient
import pandas as pd

class Course:

	def __init__(self, *args):
		self.UID, self.crn, self.course_num,\
		self.section_num, self.campus, self.num_credit,\
		self.course_title, self.days, self.startTime,\
		self.endTime, self.cap, self.wl_cap, self.instructor_name,\
		self.startDate, self.endDate, self.location, self.attribute = args
		self.lab = list()
		self.act = list()
		self.wl_act = list()

	def __init__(self, dictionary):
		self.UID = dictionary["CRN"]
		self.crn = dictionary["CRN"]
		self.course_num = dictionary["Crse"]
		self.section_num = dictionary["Sec"]
		self.campus = dictionary["Cmp"]
		self.num_credit = dictionary["Cred"]
		self.course_title = dictionary["Title"]
		self.days = dictionary["Days"]
		self.startTime = dictionary["Time"][:8]
		self.endTime = dictionary["Time"][9:]
		self.cap = dictionary["Cap"]
		self.wl_cap = dictionary["WL Cap"]
		self.instructor_name = dictionary["Instructor"]
		self.startDate = dictionary["Date"][:5]
		self.endDate = dictionary["Date"][6:]
		self.location = dictionary["Location"]
		self.attribute = dictionary["Attribute"]

class Instructor:
	def __init__(self, firstName, middleName, lastName):
		self.firstName = firstName
		self.middleName = middleName
		self.lastName = lastName
		self.website = ''
		self.email = ''
		self.department = list()
		self.relatedCourse = dict()

class Department:
	def __init__(self, deptName):
		self.deptName = deptName
		self.courses = list()

class Lab:
	def __init__(self, *args):
		self.UID, self.days, self.startTime,\
		self.endTime, self.startDate, self.endDate,\
		self.instructor, self.location = args

def main():
	###Don't forget to put all the .json file in the current dir
	current_path = inspect.getfile(inspect.currentframe())
	current_path = current_path.replace('\\', '/')
	dir_name = os.path.dirname(current_path)
	file_abs_path = os.path.abspath(dir_name) + "\\"

	file_abs_path += input("Please enter YYYY_QQQQ_School (Example 2018_Winter_De_Anza):\n")
	file_abs_path += "_courseData.json"

	if file_abs_path:
		with open(file_abs_path, 'r') as f:
			course_raw_data = json.load(f)

	clist = []
	dlist = []
	total_course = 0
	for department in course_raw_data["2018 Winter De Anza"]["CourseData"]:
		dep_course_num = 0
		temp_dept = Department(department)
		for c in course_raw_data["2018 Winter De Anza"]["CourseData"][department]:
			dep_course_num += 1
			temp_course = Course(c)
			clist.append(temp_course)
			interesting_name = temp_dept.deptName + " " + temp_course.course_num + " " + temp_course.course_title 
			if interesting_name not in temp_dept.courses:
				temp_dept.courses.append(interesting_name)
			total_course += 1
		print('department', department, "has", dep_course_num, "sections.")
		dlist.append(temp_dept)

	print('total course:', total_course)
	print('loaded course:', len(clist))

	username = input("Enter your username:")
	password = input("Password:")
	client = MongoClient("mongodb+srv://" + username +":" + password + "@fhdatimedb-jjsjm.mongodb.net/test?retryWrites=true&w=majority")
	db = client.get_database('Instructor')
	tc = db.new_test_courses
	td = db.new_test_depts
	for course in clist:
		temp_course = {
			'UID' : course.UID,
			'crn': course.crn,
			'course_num' : course.course_num,
			'section_num' : course.section_num,
			'campus' : course.campus,
			'num_credit' : course.num_credit,
			'course_title' : course.course_title,
			'days' : course.days,
			'start_time' : course.startTime,
			'end_time' : course.endTime,
			'cap' : course.cap,
			'wl_cap' : course.wl_cap,
			'instructor_name' : course.instructor_name,
			'start_date' : course.startDate,
			'end_date' : course.endDate,
			'location' : course.location,
			'attribute' : course.attribute,
		}
		tc.insert_one(temp_course)

	for dept in dlist:
		temp_dept = {
			'department_name' : dept.deptName,
			'course_list' : dept.courses
		}
		td.insert_one(temp_dept)

if __name__ == "__main__":
	main()
