

class Subject:
# Subject
# 	id
# 	name
# 	star
# 	week_num
# 	batch_name

	def __init__(self):
		self.name = ""
		self.week_num = -1
		self.batch_name = ""

	def set_star(self,number):
		self.star = number
			
	def get_star(self):
	# 	ideally read star from mongo
		return self.star

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_week(self, week_no):
		self.week_num = week_no

	def get_week(self):
		return self.week_num

	def set_batch(self, batchname):
		self.batch_name = batchname

	def get_batch(self):
		return self.batch_name

	def __str__(self):

		jsoned = {
					"name" : self.get_name(),
					"weeknum" : self.get_week(),
					"batchname" : self.get_batch(),
					"star" : self.get_star()
				}
		return jsoned
