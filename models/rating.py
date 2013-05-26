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
		self.star = -1

	def __init__(self, subj_name, date, batch, user, sem, star):
		self.name = subj_name
		self.date = date
		self.batch_name = batch
		self.username = user
		self.sem = int(sem)
		self.star = int(star)

	def set_star(self,number):
		self.star = int(number)
			
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
		self.date = datetime.datetime(int(dates[2]),int(dates[1]),int(dates[0]))
		# self.date = date_no
		


	def set_username(self, uname):
		self.username = uname

	def set_sem(self, semno):
		self.sem = int(semno)

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
			date_format = self.date.strftime("%d_%m_%Y")
		else:
			date_format = self.date
		jsoned = {
					'subject_name' : self.get_name(),
					'star' : self.get_star(),
					'date' : date_format,
					'batch' : self.get_batch(),
					'user' : self.get_username(),
					'sem' : self.get_sem()
				}
		return jsoned

		# db.ratings.aggregate({$match:{'subject_name':'s/w arch','sem':6}},{$group:{_id:{'subject':'$subject_name','sem':'$sem'},sum:{$sum:'$star'}}},{$group:{_id:{'subject':'$_id.subject','sem':'$_id.sem'},avg:{$avg:'$sum'}}})
		# db.ratings.aggregate({$group:{_id:{'subject':'$subject_name','sem':'$sem','batch':'$batch'},star_sum:{$sum:'$star'},star_avg:{$avg:'$star'}}})
