__author__ = 'raghothams'

import pymongo
import json
import subjectDAO
from subject import Subject
from user import User

def main():
	connection_string = "mongodb://localhost"
	connection = pymongo.MongoClient(connection_string)
	database = connection.starleague

	# print "got connection"
	subject_dao = subjectDAO.SubjectDAO(database)
	
	try:
		
		# subjects = subject_dao.get_all_subjects()
		# subjects = subject_dao.get_subjects_by_batch("2011-2013")
		# for subject in subjects:
		# 	print subject
		# 	print json.dumps(subject.__dict__)
		
		user = User()
		user.set_name("jake")
		user.set_batch("2010-2014")
		user.set_password("harper")



		# result = subject_dao.insert_subject(subject)
		# print result

	except Exception, e:
		print e

main()