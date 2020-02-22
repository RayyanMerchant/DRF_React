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

API_ENDPOINT = "https://weather.ls.hereapi.com/weather/1.0/report.json"


# data = {
	# 'apiKey' : 'hnxn-hc6r876FaoJIkHqp1ci8DsLAe4yKllYAPPGMGo',
	# 'product' : 'observation',
	# 'name' : 'Berlin',
# } 

data = {
	'apiKey' : 'hnxn-hc6r876FaoJIkHqp1ci8DsLAe4yKllYAPPGMGo',
	'query' : 'Pariser 1 Berl',
	'beginHighlight' : '<b>',
	'endHighlight' : '</b>',
} 

r = requests.get(url = API_ENDPOINT, params = data) 

response = r.json()
print("staus code is : ", r.status_code)
print("The response is:%s"%response) 




