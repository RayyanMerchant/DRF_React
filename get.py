import requests 
import random 
# import json
# API_ENDPOINT = "http://localhost:8000/api/calc/"
# data = {

# } 

API_ENDPOINT = "http://localhost:8000/api/pending_task/"


data = {
	'id' : '3',
} 

r = requests.get(url = API_ENDPOINT, data = data) 

response = r.json()
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




