from subject import Subject
# import pymongo

class SubjectDAO:

	def __init__(self, database):
		self.db = database
		self.subject_collection = self.db.subjects

	def get_subjects_by_batch(self, batch):
		print "in get by name"
		collection = self.subject_collection
		subjects = collection.find({"batchname":batch})

		modelled_subject_arr = []
		for subject in subjects:
			# model data from subject
			
			# print subject
			model_subject = Subject()
			model_subject.set_name(subject["name"])
			model_subject.set_star(subject["star"])
			model_subject.set_batch(subject["batchname"])
			model_subject.set_week(subject["weeknum"])
			
			# append modelled subject to array
			modelled_subject_arr.append(model_subject)

		return modelled_subject_arr
		
	def get_all_subjects(self):
		collection = self.subject_collection
		subjects = collection.find()

		modelled_subject_arr = []
		for subject in subjects:
			# model data from subject
			
			# print subject
			model_subject = Subject()
			model_subject.set_name(subject["name"])
			model_subject.set_star(subject["star"])
			model_subject.set_batch(subject["batchname"])
			model_subject.set_week(subject["weeknum"])
			
			# append modelled subject to array
			modelled_subject_arr.append(model_subject)
		
		return modelled_subject_arr

	def insert_subject(self, subject):
		
		collection = self.subject_collection
		# print(subject.__str__())
		result = collection.insert(subject.__str__())
		return result

	



	

	


