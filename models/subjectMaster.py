__author__ = 'raghothams'

# SubjectMaster
# 	name
# 	faculty
# 	semA

import json

class SubjectMaster:

	def __init__(self):
		self.name = ""
		self.faculty = ""
		self.sem = -1

	def set_name(self, subj_name):
		self.name = subj_name

	def set_faculty(self, teacher):
		self.faculty = teacher

	def set_sem(self, sem_no):
		self.sem = sem_no

	def get_name(self):
		return self.name

	def get_faculty(self):
		return self.faculty

	def get_sem(self):
		return self.sem

	def __str__(self):

		jsoned = {
					'name' : self.get_name(),
					'faculty' : self.get_faculty(),
					'sem' : self.get_sem()
				}

		return jsoned

	# def __repr__(self):
	# 	return json.dumps(self.__dict__)