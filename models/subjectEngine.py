import signal
from subjectDAO import SubjectDAO
from subject import Subject

# Class SubjectEngine
# init(st_date, e_date)
# 	start_date = st_date
# 	end_date = e_date
	

# add_subject_instance()
# 
# 	for each batch
# 		get subjects
# 		create new instances of subjects for new week
# 		insert into db
# 	finally call start_timer() to tigger alarm for next week class

# start_timer()
	# check if limit reached 
	# if NO
	# 	get the number of seconds till saturday 18:00
	# 	tigger an alarm signal with the number of seconds
	# 	pass add_subject_insatnce as signal handler
	# if YES
	# 	DoNothing
