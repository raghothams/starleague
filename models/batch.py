

class Batch:
# Batch
# 	id
# 	desc

	def __init__(self):
		self.id = ""
		self. desc = ""

	def set_id(self, id):
		self.id = id

	def set_desc(self, description):
		self.desc = description

	def get_id(self):
		return self.id

	def get_desc(self):
		return self.desc

	def __str__(self):
		jsoned = {
					'_id' : self.get_id(),
					'desc' : self.get_desc()
				}
		return jsoned