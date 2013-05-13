import pymongo
from batch import batch

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