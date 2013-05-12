from user import User

class UserDAO:

	def __init__(self, database):
		self.db = database
		self.user_collection = self.db.users

	def add_user(self, user):

		collection = self.user_collection
		result = collection.insert(user.__str__())

		return result