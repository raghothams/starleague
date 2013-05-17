__author__ = "raghothams"

import pymongo
import sessionDAO
import userDAO
import bottle
import re	#regex
import cgi	#used for content type, length, form etc
import json
from batchDAO import BatchDAO

@bottle.get('/serverTest')
def server_test():

	bottle.response.content_type = "application/json"
	return "{'status':'true'}"

@bottle.get('/batch')
def get_batches():
	result = batches.get_all_batches()
	bottle.response.content_type = "application/json"

	json_result = json.dumps(result.__dict__)
	return result


connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.starleague

batches = BatchDAO(database)

bottle.debug(True)
bottle.run(host='localhost',port=8082)