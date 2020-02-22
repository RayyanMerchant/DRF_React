import requests 
import random 
import time
# import json
API_ENDPOINT = "http://localhost:8000/api/assignment/"


# data to be sent to api 
data = {
	'task':'task no : ' + str(random.randint(1, 100)), 
	'content' : 'this is some stupid content',
	'submission_date':'29/04/2019',
} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response json  
response = r.json()
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




