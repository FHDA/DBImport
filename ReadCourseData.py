import os, json
import os,inspect
from pymongo import MongoClient
import pandas as pd

class Course:

	def __init__(self, *args):

		if isinstance(*args,dict):
			info_dict = args[0] ## args is tuple
			self.UID = info_dict["CRN"]
			self.crn = info_dict["CRN"]
			self.course_num = info_dict["Crse"]
			self.section_num = info_dict["Sec"]
			self.campus = info_dict["Cmp"]
			self.num_credit = info_dict["Cred"]
			self.course_title = info_dict["Title"]
			self.days = info_dict["Days"]
			self.startTime = info_dict["Time"][:8]
			self.endTime = info_dict["Time"][9:]
			self.cap = info_dict["Cap"]
			self.wl_cap = info_dict["WL Cap"]
			self.instructor_name = info_dict["Instructor"]
			self.startDate = info_dict["Date"][:5]
			self.endDate = info_dict["Date"][6:]
			self.location = info_dict["Location"]
			self.attribute = info_dict["Attribute"]
		else:
			self.UID, self.crn, self.course_num,\
			self.section_num, self.campus, self.num_credit,\
			self.course_title, self.days, self.startTime,\
			self.endTime, self.cap, self.wl_cap, self.instructor_name,\
			self.startDate, self.endDate, self.location, self.attribute = args
			self.lab = list()
			self.act = list()
			self.wl_act = list()

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
	current_path = os.path.abspath('.')
	current_path = current_path.replace('\\', '/')
	print(current_path)
	allfiles= os.listdir(current_path)
	print(allfiles)
	#file_abs_path = os.path.abspath(current_path) + "\\"
	

	username = input("Enter your username:")
	password = input("Password:")
	client = MongoClient("mongodb+srv://" + username +":" + password + "@fhdatimedb-jjsjm.mongodb.net/test?retryWrites=true&w=majority")

	for i in range(len(allfiles)):
		if os.path.splitext(allfiles[i])[1] != ".json":
			continue
		file_path = ""
		file_path = current_path + '/'
		database_name = os.path.splitext(allfiles[i])[0]
		file_path = file_path + allfiles[i]

		if file_path:
			with open(file_path, 'r') as f:
				course_raw_data = json.load(f)

		clist = []
		dlist = []
		total_course = 0

		#index_name = database_name
		temp_arr = database_name.split('_')
		index_name = temp_arr[0] + " " + temp_arr[1] + " " + temp_arr[2] + " " + temp_arr[3]

		for department in course_raw_data[index_name]["CourseData"]:
			dep_course_num = 0
			temp_dept = Department(department)
			for c in course_raw_data[index_name]["CourseData"][department]:
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


		db = client.get_database(database_name)
		course_subbase = db.Courses
		dept_subbase = db.Department
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
			course_subbase.insert_one(temp_course)

		for dept in dlist:
			temp_dept = {
				'department_name' : dept.deptName,
				'course_list' : dept.courses
			}
			dept_subbase.insert_one(temp_dept)

if __name__ == "__main__":
	main()
