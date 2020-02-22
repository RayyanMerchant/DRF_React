import requests 
import random 
# import json
# API_ENDPOINT = "http://localhost:8000/api/calc/"
# data = {

# } 

# API_ENDPOINT = "http://localhost:8000/api/pending_task/"


# data = {
	# 'id' : '5',
# } 

# API_ENDPOINT = "https://autocomplete.geocoder.ls.hereapi.com/6.2/suggest.json"

# data = {
	# 'apiKey' : 'hnxn-hc6r876FaoJIkHqp1ci8DsLAe4yKllYAPPGMGo',
	# 'product' : 'observation',
	# 'name' : 'Berlin',
# } 


# API_ENDPOINT = "https://places.sit.ls.hereapi.com/places/v1/autosuggest"

# data = {
	# 'apiKey' : 'hnxn-hc6r876FaoJIkHqp1ci8DsLAe4yKllYAPPGMGo',
	# 'at' : '40.74917,-73.98529',
	# 'q' : 'chrysler',
# } 

API_ENDPOINT =  "https://geocoder.ls.hereapi.com/6.2/geocode.json"

data = {
	'apiKey' : 'hnxn-hc6r876FaoJIkHqp1ci8DsLAe4yKllYAPPGMGo',
	'searchtext' : 'dadar mumbai',
} 


r = requests.get(url = API_ENDPOINT, params = data) 

response = r.json()
lat = response['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
long = response['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
print("Latitude = ", lat)
print("Longitude = ", long)
print(lat, long)
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




