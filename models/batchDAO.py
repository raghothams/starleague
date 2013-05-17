import pymongo
from batch import Batch
from subjectMaster import SubjectMaster
import json

class BatchDAO:

	def __init__(self, database):
		self.db = database
		self.batch_coll = self.db.batches

	def add_batch(self, modelled_batch):
		
		collection = self.batch_coll
		result = collection.insert(modelled_batch.__str__())

		return result

	def delete_batch(self, modelled_batch):

		collection = self.batch_coll
		result = collection.remove({'_id':modelled_batch.get_id()})

		return result

	def get_all_batches(self):

		collection = self.batch_coll
		result = collection.find()

		batches = []
		for item in result:
			
			single_batch = Batch()
			
			single_batch.set_id(item['_id'])
			single_batch.set_desc(item['desc'])
			single_batch.set_current_sem(item['current_sem'])
			single_batch.set_subject_array(self.construct_subject_master(item))

			batches.append(single_batch)

		print json.dumps(batches, default=Batch.__str__)
		return batches

	def construct_subject_master(self, pymongo_batch):

		modelled_subject_master_array = []
		subjects = pymongo_batch['subject_master']
		
		for item in subjects:
			modelled_subject = SubjectMaster()
			
			modelled_subject.set_name(item['name'])
			modelled_subject.set_sem(item['sem'])
			modelled_subject.set_faculty(item['faculty'])

			modelled_subject_master_array.append(modelled_subject)

		return modelled_subject_master_array 