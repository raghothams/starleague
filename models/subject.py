

class Subject:
__author__ = 'raghothams'

# Subject
# 	id
# 	name
# 	star
# 	date
# 	batch_name
# 	published

	def __init__(self):
		self.name = ""
		self.date = -1
		self.batch_name = ""
		published = false

	def set_star(self,number):
		self.star = number
			
	def get_star(self):
	# 	ideally read star from mongo
		return self.star

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_date(self, date_no):
		self.date = date_no

	def set_published(self, status):
		self.published = status

	def get_date(self):
		return self.date

	def set_batch(self, batchname):
		self.batch_name = batchname

	def get_batch(self):
		return self.batch_name

	def is_published(self):
		return self.published

	def __str__(self):

		jsoned = {
					"name" : self.get_name(),
					"date" : self.get_date(),
					"batchname" : self.get_batch(),
					"star" : self.get_star(),
					"published" : self.is_published()
				}
		return jsoned
