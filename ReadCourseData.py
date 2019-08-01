import json
from pymongo import MongoClient

class Course:
	def __init__(self, crn):
		self.crn = crn

	def __init__(self, UID, crn, course_num, section_num,\
		campus, num_credit, course_title, days, startTime, endTime, cap, wl_cap, \
		instructor_name, startDate, endDate, location, attribute = ''):
		self.UID = UID
		self.crn = crn
		self.course_num = course_num
		self.section_num = section_num
		self.campus = campus
		self.num_credit = num_credit
		self.course_title = course_title
		self.days = days
		self.startTime = startTime
		self.endTime = endTime
		self.cap = cap
		self.wl_cap = wl_cap
		self.instructor_name = instructor_name
		self.startDate = startDate
		self.endDate = endDate
		self.location = location
		self.attribute = attribute
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
	def __init__(self, UID, days, startTime, endTime, \
				startDate, endDate, instructor, location):
		self.UID = UID
		self.days = days
		self.startTime = startTime
		self.endTime = endTime
		self.startDate = startDate
		self.endDate = endDate
		self.instructor = instructor
		self.location = location



def main():

	filename = 'E:\\Personal_Workflow\\FHDA\\'
	filename += input("Please enter YYYY_QQQQ_School (Example 2018_Winter_De_Anza):\n")
	filename += "_courseData.json"

	if filename:
		with open(filename, 'r') as f:
			course_raw_data = json.load(f)

	clist = []
	dlist = []
	total_course = 0
	for department in course_raw_data["2018 Winter De Anza"]["CourseData"]:
		dep_course_num = 0
		temp_dept = Department(department)
		for c in course_raw_data["2018 Winter De Anza"]["CourseData"][department]:
			dep_course_num += 1
			temp_course = Course(c["CRN"], c["CRN"], c["Crse"], c["Sec"], c["Cmp"], c["Cred"],
							 c["Title"], c["Days"], c["Time"][:8], c["Time"][9:], c["Cap"], 
							 c["WL Cap"], c["Instructor"], c["Date"][:5], c["Date"][6:],
							 c["Location"], c["Attribute"])
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
	db = client.get_database('yifeil_test')
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