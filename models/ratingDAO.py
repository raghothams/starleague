__author__ = 'raghothams'

from rating import Rating
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

	def insert_Rating(self, rating):
		
		collection = self.rating_collection
		# print(Rating.__str__())
		result = collection.insert(rating.__str__())
		return result

	



	

	


