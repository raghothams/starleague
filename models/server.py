__author__ = "raghothams"

import pymongo
import sessionDAO
import userDAO
import bottle
import re	#regex
import cgi	#used for content type, length, form etc
import json
import operator
from user import User
from batch import Batch
from batchDAO import BatchDAO
from sessionDAO import SessionDAO
from userDAO import UserDAO
from ratingDAO import RatingDAO
from subjectMaster import SubjectMaster
from responseWrapper import ResponseWrapper


@bottle.route('/index.html')
def render_index():
	return bottle.template('index')

@bottle.route('/welcome.html')
def render_welcome():
	return bottle.template('welcome')

@bottle.route('/signup.html')
def render_signup():
	return bottle.template('signup')

@bottle.route('/static/<filename:path>', name='static')
def static_server(filename):
	return bottle.static_file(filename, root='static')

@bottle.get('/app/servertest')
def server_test():

	bottle.response.content_type = "application/json"
	return '{"status":true}'

@bottle.get('/app/batch')
# get all batches
def get_batches():
	result = batches.get_all_batches()
	wrapped_response = ResponseWrapper()

	# print result
	bottle.response.content_type = "application/json"
	json_result = None

	if result != None :
		wrapped_response.set_data(result)
		wrapped_response.set_error(False)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
	
	else:
		wrapped_response.set_error(True)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)

	return json_result


@bottle.get('/app/signup')
def render_singup():
	return "signup with username and password"



@bottle.get('/app/batch/<batchid>')
# get the specified batch
def get_batch(batchid):
	
	result = batches.get_batch_by_id(batchid)
	bottle.response.content_type = "application/json"
	
	array = [result]
	wrapped_response = ResponseWrapper()
	json_result = None
	
	if result != None :
		wrapped_response.set_data(array)
		wrapped_response.set_error(False)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
	
	else:
		wrapped_response.set_error(True)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)

	return json_result

@bottle.get('/app/myinfo')
def app_info():
	result = get_myinfo()
	
	if result != None:
		wrapped_response = ResponseWrapper()
		wrapped_response.set_error(False)
		wrapped_response.set_data(result)

		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
		return json_result

	else:
		wrapped_response = ResponseWrapper()
		wrapped_response.set_error(True)
		wrapped_response.set_data([])

		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
		return json_result


@bottle.get('/app/myratings')
def get_myratings():

	cookie = bottle.request.get_cookie("session")
	username = sessions.get_username(cookie)  # see if user is logged in

	result = ratings.get_user_ratings(username)

	wrapped_response = ResponseWrapper()
	json_result = None

	if result != None :
		wrapped_response.set_data(result)
		wrapped_response.set_error(False)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
	
	else:
		wrapped_response.set_error(True)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)

	bottle.response.content_type = "application/json"
	return json_result

@bottle.get('/app/myratings/sem/<semno>')
def get_myratings_by_sem(semno):

	cookie = bottle.request.get_cookie("session")
	username = sessions.get_username(cookie)  # see if user is logged in
	print username, semno
	result = ratings.get_user_ratings_by_sem(username,semno)

	wrapped_response = ResponseWrapper()
	json_result = None

	if result != None :
		wrapped_response.set_data(result)
		wrapped_response.set_error(False)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
	
	else:
		wrapped_response.set_error(True)
		json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)

	bottle.response.content_type = "application/json"
	return json_result


@bottle.get('/app/leaderboard/subject/<subj>/sem/<semno>')
def get_average_for_subject(subj, semno):

	result = ratings.get_average_rating_by_subject(subj, semno)
	serialized = None
	
	if result != None:
		serialized = { "error":False,
					"data":result
				}
	else:
		serialized = { "error":True,
					"data":""
				}
	
	bottle.response.content_type = "application/json"
	return json.dumps(serialized)


@bottle.get('/app/leaderboard')
def get_average_for_subject():
	# get current sem for each batch.
	# get average ratings for all subjects in current sem

	serialized = None
	running_batches = batches.get_all_running_batches()
	sem_subjects_combo = get_current_sem_subjects(running_batches)
	# print sem_subjects_combo
	if sem_subjects_combo != None:

		result = []
		for item in sem_subjects_combo:		
			
			temp_result = ratings.get_average_rating_by_subject(item.get_name(),item.get_sem())
			temp_result['faculty'] = item.get_faculty()
			if temp_result != None:
				result.append(temp_result)
			else:
				serialized = { "error":True,
						"data":""
					}
		# sort the results
		# sorted(student_tuples, key=lambda student: student[2]) 
		# print result
		# sorted_list = sorted(result, key=lambda item: item.result[0].avg)
		# print sorted_list

		serialized = { "error":False,
						"data":result
					}
	else:
			serialized = { "error":True,
						"data":""
					}	

	# print json.dumps(serialized)
	bottle.response.content_type = "application/json"
	return json.dumps(serialized)


# handles a login request
@bottle.post('/app/login')
def process_login():

    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print "user submitted ", username

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])

        if session_id is None:
            # bottle.redirect("/internal_error")
            return "Internal error"

        cookie = session_id

        # Warning, if you are running into a problem whereby the cookie being set here is
        # not getting set on the redirect, you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie("session", cookie)
        return "success logging in"
        # bottle.redirect("/welcome")

    else:
        # return bottle.template("login",
        #                        dict(username=cgi.escape(username), password="",
        #                             login_error="Invalid Login"))
		return "error logging in"



@bottle.post('/app/signup')
def process_signup():

	email = bottle.request.forms.get("email")
	username = bottle.request.forms.get("username")
	password = bottle.request.forms.get("password")
	verify = bottle.request.forms.get("verify")
	batch = bottle.request.forms.get("batch")
	user_type = bottle.request.forms.get("type")


    # set these up in case we have an error case
	errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
	if validate_signup(username, password, verify, email, errors):

		#create a modelled user
		temp_user = User(email, username, password, batch, user_type)
		if not users.add_user(temp_user):
			# this was a duplicate
			errors['username_error'] = "Username already in use. Please choose another"
			return bottle.template("signup", errors)

		session_id = sessions.start_session(username)
		print session_id
		bottle.response.set_cookie("session", session_id)
		bottle.redirect("/welcome")
	else:
		print "user did not validate"
		return bottle.template("signup", errors)



@bottle.get("/app/welcome")
def present_welcome():
	# check for a cookie, if present, then extract value

	cookie = bottle.request.get_cookie("session")
	username = sessions.get_username(cookie)  # see if user is logged in
	if username is None:
		# print "welcome: can't identify user...redirecting to signup"
		return "welcome: can't identify user...redirecting to signup"
	else:
		result = get_myinfo(username)
		dummy_list = []
		if result != None:
			# dummy_list.append(result)
			# wrapped_response = ResponseWrapper()
			# wrapped_response.set_error(False)
			# wrapped_response.set_data(dummy_list)
			wrapper_response = { 
								'error':False,
								'data':result
			}
			# json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
			json_result = json.dumps(wrapper_response)
			bottle.response.content_type="application/json"
			return json_result
		else:
			wrapped_response = ResponseWrapper()
			wrapped_response.set_error(True)
			wrapped_response.set_data([])

			json_result = json.dumps(wrapped_response, default=ResponseWrapper.__str__)
			return json_result

	


# Helper Functions

# validates that the user information is valid for new signup, return True of False
# and fills in the error string if there is an issue
def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error'] = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""

    if not USER_RE.match(username):
        errors['username_error'] = "invalid username. try just letters and numbers"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "invalid password."
        return False
    if password != verify:
        errors['verify_error'] = "password must match"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "invalid email address"
            return False
    return True

def get_current_sem_subjects(batch_cursor):

	result = []
	for item in batch_cursor:

		current_sem = item['current_sem']
		subject_list = item['subject_master']

		for subject_item in subject_list:
			if subject_item['sem'] == current_sem:
				subject = SubjectMaster(subject_item['name'], subject_item['faculty'], subject_item['sem'])
				result.append(subject)

	return result

def get_myinfo(username):

	# get username, batch, type from users
	# get current sem from batches
	user_result = users.get_user_by_id(username)

	if user_result != None:
		batch_result = batches.get_batch_by_id(user_result['batch'])

		if batch_result != None:
			current_sem = batch_result.get_current_sem()

			if current_sem != None:
				# temp_user = User("",user_result['_id'],"",user_result['batch'],user_result['type'])
				temp_user = {
								'username':user_result['_id'],
								'batch':user_result['batch'],
								'type':user_result['type'],
								'current_sem':current_sem
							}
				return temp_user
	return None





connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.starleague

batches = BatchDAO(database)
users = UserDAO(database)
sessions = SessionDAO(database)
ratings = RatingDAO(database)

bottle.debug(True)
bottle.run(host='localhost',port=8082)