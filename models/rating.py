

class Rating:
__author__ = 'raghothams'

# Rating
# 	id
# 	name
# 	star
# 	date
# 	batch_name
# 	user
#	sem

	def __init__(self):
		self.name = ""
		self.date = -1
		self.batch_name = ""
		self.username = ""
		self.sem = -1

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

	def set_username(self, uname):
		self.username = uname

	def set_sem(self, semno):
		self.sem = semno

	def get_date(self):
		return self.date

	def set_batch(self, batchname):
		self.batch_name = batchname

	def get_batch(self):
		return self.batch_name

	def get_username(self):
		return self.username()

	def get_sem(self):
		return self.sem

	def __str__(self):

		jsoned = {
					"subject_name" : self.get_name(),
					"star" : self.get_star(),
					"date" : self.get_date(),
					"batch" : self.get_batch(),
					"user" : self.get_username(),
					"sem" : self.get_sem()
				}
		return jsoned
