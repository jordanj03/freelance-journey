import requests

# r = requests.get("https://httpbin.org/status/400")
r = requests.get("https://httpbin.org/json")

if r.status_code != 200:
	print("API request returned a non-success response")
else:
	data = r.json()
	print(data)
