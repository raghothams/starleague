

class Batch:
# Batch
# 	id
# 	desc
# 	current_sem
	# "subjects":
		# [
		# 	{
		# 		"name" : "abc"
		# 		"faculty" : "qwer"
		# 		"sem" : 6
		# 	},
		# 	{
		# 		"name" : "foo"
		# 		"faculty" : "bar"
		# 		"sem" : 6
		# 	}
		# ]

	def __init__(self):
		self.id = ""
		self. desc = ""
		self.current_sem = -1
		self.subjects = []

	def set_id(self, id):
		self.id = id

	def set_desc(self, description):
		self.desc = description

	def set_current_sem(self, sem):
		self.current_sem = sem

	def set_subject_array(self, subject_master_array):
		self.subjects = subject_master_array

	def append_subject_array(self, subject_master):
		self.subjects.append(subject_master)

	def get_id(self):
		return self.id

	def get_desc(self):
		return self.desc

	def get_current_sem(self):
		return self.current_sem

	def get_subjects_array(self):
		return self.subjects

	def __str__(self):
		jsoned = {
					'_id' : self.get_id(),
					'desc' : self.get_desc(),
					'current_sem' : self.get_current_sem(),
					'subject_master' : self.get_subjects_array()
				}
		return jsoned