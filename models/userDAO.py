__author__ = 'raghothams'

from user import User
# import hmac
import pymongo
import hashlib
import random

class UserDAO:

	def __init__(self, database):
		self.db = database
		self.user_collection = self.db.users
		# self.SECRET = 'thisissuperdupersecret'

	def make_salt(self):
		salt = ""
		for i in range(5):
			salt = salt + random.choice(string.ascii_letters)
		return salt

	def make_pw_hash(self, pw, salt=None):
		if salt == None:
			salt = self.make_salt()
		return hashlib.sha256(pw + salt).hexdigest()+","+salt

	def validate_login(self, uname, pw):

		user = None
		try:
			collection = self.user_collection
			user = collection.find_one({"_id":username})

		except:
			print "error finding user"

		if user is None:
			print "User not in database"
			return None

		password = user["password"]
		salt = password.split(',')[1]

		# Check if the user password matches
		if password != self.make_pw_hash(pw, salt):
			print "user password is not a match"
			return None

		# User password matches. Return user
		return user

	def add_user(self, modelled_user):

		password_hash = self.make_pw_hash(modelled_user.get_password())

		user = {
					'_id' : modelled_user.get_name(),
					'password' : password_hash,
					'email' : modelled_user.get_email,
					'batch' : modelled_user.get_batch()
				}

		try:
			collection = self.user_collection
			result = collection.insert(user)

		except pymongo.errors.OperationFailure:
			print "oops, mongo error"
			return False
		except pymongo.errors.DuplicateKeyError as e:
			print "oops, username already taken"
			return False

		return True
