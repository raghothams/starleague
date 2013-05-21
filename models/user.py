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
		self.batch = ""
		self.email = ""
		self.type = ""

	def __init__(self, email, uname, pwd, batch, usertype):
		self.name = uname
		self.email = email
		self.password = pwd
		self.batch = batch
		self.type = usertype

	def set_name(self, name):
		self.name = name

	def set_password(self, pwd):
		self.password = pwd

	def set_batch(self, batch):
		self.batch = batch

	def set_email(self, email):
		self.email = email

	def set_type(self,usertype):
		self.type = usertype

	def get_name(self):
		return self.name

	def get_password(self):
		return self.password

	def get_batch(self):
		return self.batch

	def get_email(self):
		return self.email

	def get_type(self):
		return self.type

	def __str__(self):
		jsoned = {
					"_id" : self.get_name(),
					"password" : self.get_password(),
					"batch" : self.get_batch(),
					"email" : self.get_email(),
					"type" : self.get_type()
				}
		return jsoned


