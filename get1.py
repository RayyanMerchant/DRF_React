import requests 
import random 
# import json
# API_ENDPOINT = "http://localhost:8000/api/calc/"
# data = {

# } 

API_ENDPOINT = "http://localhost:8000/api/teacher_left/"


data = {
	'id' : '5',
} 



r = requests.get(url = API_ENDPOINT, params = data) 

response = r.json()

# lat = response['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
# long = response['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
# print("Latitude = ", lat)
# print("Longitude = ", long)
# print(lat, long)


print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




