#This tool/prject is import json file class info fetch from De Anza College / Foothill College portal
#to MongoDB database.


import json
import os
import logging 
import inspect
from pymongo import MongoClient
from pathlib import Path 
from dotenv import load_dotenv

class Course:

	def __init__(self, **kwargs):
		self.UID = kwargs.get('UID')
		self.crn = kwargs.get('crn')
		self.course_num = kwargs.get('course_num')
		self.section_num = kwargs.get('section_num')
		self.campus = kwargs.get('campus')
		self.num_credit = kwargs.get('num_credit')
		self.course_title = kwargs.get('course_title')
		self.days = kwargs.get('days')
		self.startTime = kwargs.get('startTime')
		self.endTime = kwargs.get('endTime')
		self.cap = kwargs.get('cap')
		self.wl_cap = kwargs.get('wl_cap')
		self.instructor_name = kwargs.get('instructor_name')
		self.startDate = kwargs.get('startDate')
		self.endDate = kwargs.get('endDate')
		self.location = kwargs.get('location')
		self.attribute = kwargs.get('attribute')
		self.lab = []
		self.act = []
		self.wl_act = []

class Instructor:
	def __init__(self, **kwargs):
		self.firstName = kwargs.get('firstName')
		self.middleName = kwargs.get('middleName')
		self.lastName = kwargs.get('lastName')
		self.website = ''
		self.email = ''
		self.department = []
		self.relatedCourse = {}

class Department:
	def __init__(self, deptName):
		self.deptName = deptName
		self.courses = []

class Lab:
	def __init__(self,**kwargs):
		self.UID = kwargs.get('UID')
		self.days = kwargs.get('days')
		self.startTime = kwargs.get('startTime')
		self.endTime = kwargs.get('endTime')
		self.startDate = kwargs.get('startDate')
		self.endDate = kwargs.get('endDate')
		self.instructor = kwargs.get('instructor')
		self.location = kwargs.get('location')

def from_raw_to_list(course_raw):
 	db = get_db()
	test_course = db.new_test_courses  
	test_department = db.new_test_depts	

	for department in course_raw[list(course_raw)[0]]['CourseData']:
		temp_dept = Department(department)
		course_ineach_dept = '{0} {1} {2}'.format(temp_dept.deptName, temp_course.course_num, temp_course.course_title) 
		if course_ineach_dept not in temp_dept.courses:
			temp_dept.courses.append(course_ineach_dept)
		test_department.insert_one(temp_dept)
    
 	 for c in course_raw[list(course_raw)[0]]['CourseData'][department]:
		temp_course = Course(UID = c['CRN'],crn = c['CRN'], course_num = c['Crse'], 
				   	  section_num = c['Sec'], campus = c['Cmp'], num_credit = c['Cred'],
		 		   	  course_title = c['Title'], days = c['Days'], startTime = c['Time'][:8], 
				   	  endTime = c['Time'][9:], cap = c['Cap'], wl_cap = c['WL Cap'],instructor_name = c['Instructor'],
                		   	  startDate = c['Date'][:5], endDate = c['Date'][6:],location = c['Location'],
                   		   	  attribute = c['Attribute'])
	  	test_course.insert_one(temp_course)
      		amount_course = 0
     		amount_course += 1

	return amount_course




def get_db():
	env_path = Path('.') / '.env'
	load_dotenv(dotenv_path=env_path)
	username = os.getenv('Mongo_User')
	password = os.getenv('Mongo_Password')
	db_name = 'yifeil_test'      #os.getenv('Mongo_DBName') #just tesing the code
	client = MongoClient('mongodb+srv://' + username +':' + password + '@fhdatimedb-jjsjm.mongodb.net/test?retryWrites=true&w=majority')
	return client.get_database(db_name)



def main():

	current_path = inspect.getfile(inspect.currentframe())
  	current_path = current_path.replace('\\', '/')
	dir_name = os.path.dirname(current_path)
	file_abs_path = os.path.join(os.path.abspath(dir_name), "\\")
  	filename = os.path.join(file_abs_path, '2019_Fall_De_Anza_courseData.json')

	if filename:
		with open(filename, 'r') as f:
			course_raw_data = json.load(f)

	amount_course = from_raw_to_list(course_raw_data)
  
	logger = logging.getLogger(_name_)
	logger.setLevel(logging.INFO)
	filehandler = logging.FileHandler("FHDA_TIME_log")
	filehandler.setLevel(logging.DEBUG)
	cmdhandler = logging.StreamHandler()
	cmdhandler.setLevel(logging.ERROR)
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	cmdhandler.setFormatter(formatter)
	filehanlder.setFormatter(formatter)
	logger.addHandler(cmdhandler)
	logger.addHandler(filehandler)
  	logging.info('Total loaded course:', amount_course)


if __name__ == '__main__':
	main()
