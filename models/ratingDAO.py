__author__ = 'raghothams'

from rating import Rating
from bson.son import SON
# import pymongo

class RatingDAO:

	def __init__(self, database):
		self.db = database
		self.rating_collection = self.db.ratings

	def get_ratings_by_batch(self, batch):
		print "in get by batch"
		collection = self.rating_collection
		ratings = collection.find({"batchname":batch})

		modelled_rating_arr = []
		for rating in ratings:
			# model data from Rating
			
			# print Rating
			model_rating = Rating()
			model_rating.set_name(rating["subject_name"])
			model_rating.set_star(rating["star"])
			model_rating.set_date(rating["date"])
			model_rating.set_batch(rating["batch"])
			model_rating.set_batch(rating["user"])
			model_rating.set_batch(rating["sem"])
			
			# append modelled Rating to array
			modelled_rating_arr.append(model_rating)

		return modelled_Rating_arr
		
	def get_all_ratings(self):
		collection = self.Rating_collection
		ratings = collection.find()

		modelled_rating_arr = []
		for rating in ratings:
			# model data from Rating
			
			# print Rating
			model_rating = Rating()
			model_rating.set_name(rating["subject_name"])
			model_rating.set_star(rating["star"])
			model_rating.set_date(rating["date"])
			model_rating.set_batch(rating["batch"])
			model_rating.set_batch(rating["user"])
			model_rating.set_batch(rating["sem"])
			
			# append modelled Rating to array
			modelled_rating_arr.append(model_rating)
		
		return modelled_rating_arr

	def get_user_ratings(self, user):
		collection = self.rating_collection
		ratings = collection.find({'user' : user})

		modelled_rating_arr = []
		for rating in ratings:
			model_rating = Rating()
			model_rating.set_name(rating["subject_name"])
			model_rating.set_star(rating["star"])
			model_rating.set_date(rating["date"])
			model_rating.set_batch(rating["batch"])
			model_rating.set_username(rating["user"])
			model_rating.set_sem(rating["sem"])

			modelled_rating_arr.append(model_rating)
		return modelled_rating_arr

	def get_user_ratings_by_sem(self, user, semno):
		collection = self.rating_collection

		ratings = collection.find({"user":user, "sem":int(semno)})

		modelled_rating_arr = []
		for rating in ratings:
			model_rating = Rating()
			model_rating.set_name(rating["subject_name"])
			model_rating.set_star(rating["star"])
			model_rating.set_date(rating["date"])
			model_rating.set_batch(rating["batch"])
			model_rating.set_username(rating["user"])
			model_rating.set_sem(rating["sem"])

			modelled_rating_arr.append(model_rating)
		print modelled_rating_arr
		return modelled_rating_arr
		

	def insert_Rating(self, rating):
		
		collection = self.rating_collection
		# print(Rating.__str__())
		result = collection.insert(rating.__str__(False))
		return result




	# to get average for all subjects
	# db.ratings.aggregate({$group:{_id:{subject:"$subject_name",sem:"$sem"},avg:{$avg:"$star"}}})	

	def get_average_rating(self):

		collection = self.rating_collection
		result = collection.aggregate([
				{"$group":{"_id":{"subject":"$subject_name", "sem":"$sem", "batch":"$batch"}, "avg":{"$avg":"$star"}}},
				{"$sort": SON({"avg":-1})}
			])

		return result



	# to get average for specified subject
	# db.ratings.aggregate({$match:{'subject_name':'sqe'}},{$group:{_id:{subject:"$subject_name",sem:"$sem"},avg:{$avg:"$star"}}})
	
	# method to get average ratings for a given subject in a semester
	def get_average_rating_by_subject(self, subject_name, semno):

		collection = self.rating_collection
		result = collection.aggregate([
				{"$match":{"subject_name":subject_name, "sem":int(semno)}},
				{"$group":{"_id":{"subject":"$subject_name", "sem":"$sem", "batch":"$batch"}, "avg":{"$avg":"$star"}}},
				{"$sort": SON({"avg":-1})}
			])
		# print result
		return result
