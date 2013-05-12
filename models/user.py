class User:
# User
# 	id
# 	name
# 	password
# 	batch_name

	def __init__(self):
		self.name=""
		self.password=""
		self.batch_name = ""

	def set_name(self, name):
		self.name = name

	def set_password(self, pwd):
		self.password = pwd

	def set_batch(self, batch):
		self.batch_name = batch

	def get_name(self):
		return self.name

	def get_password(self):
		return self.password

	def get_batch(self):
		return self.batch_name

	def __str__(self):
		jsoned = {
					"name" : self.get_name(),
					"password" : self.get_password(),
					"batchname" : self.get_batch()
				}


