import json
import requests
import os

r = requests.get('https://httpbin.org/json')

if r.status_code != 200:
	print("API call failed")
	exit()

jsonFilePath = 'test.json'
jsonRequest = r.json()

if not os.path.exists(jsonFilePath):
	print(f"{jsonFilePath} not found.")
	exit()

with open('test.json') as f:
	jsonString = json.load(f)

print(jsonString)
print(jsonRequest)
print("------------------")
merged_json = jsonString | jsonRequest
print(json.dumps(merged_json, indent=4))