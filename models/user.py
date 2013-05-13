__author__ = 'raghothams'

class User:
# User
# 	name
# 	password
# 	batch_name
#	email

	def __init__(self):
		self.name=""
		self.password=""
		self.batch_name = ""
		self.email = ""

	def set_name(self, name):
		self.name = name

	def set_password(self, pwd):
		self.password = pwd

	def set_batch(self, batch):
		self.batch_name = batch

	def set_email(self, email):
		self.email = email

	def get_name(self):
		return self.name

	def get_password(self):
		return self.password

	def get_batch(self):
		return self.batch_name

	def get_email(self):
		return self.email

	def __str__(self):
		jsoned = {
					"name" : self.get_name(),
					"password" : self.get_password(),
					"batchname" : self.get_batch(),
					"email" : self.get_email()
				}


