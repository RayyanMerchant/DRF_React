import requests 
import random 
# import json
API_ENDPOINT = "http://localhost:8000/api/calc/"


# data to be sent to api 
data = {
	'result':-500, 
	'num1':random.randint(1, 1000), 
	'num2':random.randint(1, 1000), 
	'newid':'741',
} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response json  
response = r.json()
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




