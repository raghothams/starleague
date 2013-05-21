import json

class ResponseWrapper:

	def __init__(self):
		self.data = None
		self.error = None
		self.typeinfo = None

	def set_data(self, data, typeinfo):
		self.data = data
		self.typeinfo = typeinfo

	def set_error(self, error):
		self.error = error

	def __str__(self):
		classname = self.typeinfo
		jsoned = {
					'error' : self.error,
					'data' : json.dumps(self.data,default=classname.__str__)
				}
		print jsoned
		return jsoned