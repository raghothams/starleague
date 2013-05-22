__author__ = 'raghothams'

import datetime

class Rating:

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
	# TO PASS DATE AS YYYY_MM_DD FORMAT
	def set_date(self, date_no):
		dates = date_no.split('_')
		self.date = datetime.datetime(dates[0],dates[1],dates[2])
		# self.date = date_no


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
		return self.username

	def get_sem(self):
		return self.sem

	def __str__(self, date_as_string=True):

		date_format = None
		if date_as_string:
			date_format = self.date.strf("%H_%m_%d")
		else:
			date_format = self.date
		jsoned = {
					"subject_name" : self.get_name(),
					"star" : self.get_star(),
					"date" : date_format,
					"batch" : self.get_batch(),
					"user" : self.get_username(),
					"sem" : self.get_sem()
				}
		return jsoned
