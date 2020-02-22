import requests 
import random 
import time
# import json
 

# API_ENDPOINT = "http://localhost:8000/api/pending_task/"
# data = {
	# 'email' : 'sad@sade.com',
# } 

# API_ENDPOINT = "http://localhost:8000/api/assignment_id/"


# data = {
	# 'id' : '5',
# } 


# API_ENDPOINT = "http://localhost:8000/api/assignment/"
# data = {
	# 'task' : 'task no : ' + str(random.randint(1, 1000)),
	# 'content' : 'this is some default content',
	# 'submission_date' : '03/10/2009',
# } 


# API_ENDPOINT = "http://localhost:8000/api/assignment_ans/"
# data = {
	# 'ans' : 'this is a new ans',
	# 'id' : '3',
# } 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response json  
response = r.json()
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




