import json
from pymongo import MongoClient

class Course:
	def __init__(self, crn):
		self.crn = crn

	def __init__(self, crn, course_num, section_num,\
		campus, num_credit, course_title, days, time, cap, act, wl_cap, wl_act, \
		instructor_name, course_duration, location, attribute = '', lab_time = []):
		self.crn = crn
		self.course_num = course_num
		self.section_num = section_num
		self.campus = campus
		self.num_credit = num_credit
		self.course_title = course_title
		self.days = days
		self.time = time
		self.cap = cap
		self.act = act
		self.wl_cap = wl_cap
		self.wl_act = wl_act
		self.instructor_name = instructor_name
		self.course_duration = course_duration
		self.location = location
		self.attribute = attribute
		self.lab_time = lab_time

def main():

	filename = 'C:\\Users\\Administrator\\Desktop\\2018_Winter_De_Anza_courseData.json'


	if filename:
		with open(filename, 'r') as f:
			course_raw_data = json.load(f)

	clist = []
	total_course = 0
	for department in course_raw_data["2018 Winter De Anza"]["CourseData"]:
		dep_course_num = 0
		for c in course_raw_data["2018 Winter De Anza"]["CourseData"][department]:
			dep_course_num += 1
			temp_course = Course(c["CRN"], c["Crse"], c["Sec"], c["Cmp"], c["Cred"],
							 c["Title"], c["Days"], c["Time"], c["Cap"], c["Act"], 
							 c["WL Cap"], c["WL Act"], c["Instructor"], c["Date"],
							 c["Location"], c["Attribute"], c["Lab Time"])
			clist.append(temp_course)
			total_course += 1
		print('department', department, "has", dep_course_num, "sections.")

	print('total course:', total_course)
	print('loaded course:', len(clist))


	client = MongoClient("mongodb+srv://yifeil:Zhirezhixin1@fhdatimedb-jjsjm.mongodb.net/test?retryWrites=true&w=majority")
	db = client.get_database('yifeil_test')
	tc = db.test1
	for course in clist:
		temp_course = {
			'crn': course.crn,
			'course_num' : course.course_num,
			'section_num' : course.section_num,
			'campus' : course.campus,
			'num_credit' : course.num_credit,
			'course_title' : course.course_title,
			'days' : course.days,
			'time' : course.time,
			'cap' : course.cap,
			'act' : course.act,
			'wl_cap' : course.wl_cap,
			'wl_act' : course.wl_act,
			'instructor_name' : course.instructor_name,
			'course_duration' : course.course_duration,
			'location' : course.location,
			'attribute' : course.attribute,
			'lab_time' : course.lab_time
		}
		tc.insert_one(temp_course)
		print("inserted")






if __name__ == "__main__":
	main()