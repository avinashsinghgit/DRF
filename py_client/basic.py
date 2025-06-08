import requests

# endpoint = "https://httpbin.org/status/200"
# response = requests.get(endpoint)
# print(response.status_code)

# endpoint = "https://httpbin.org/anything"
# get_response = requests.get(endpoint)
# # print(get_response.text)
# print(get_response.json())

# HTTP request => HTML
# REST API HTTP REQUEST => JSON


endpoint ="http://127.0.0.1:8000/api/"
params= {"password" : "avinash123"}
payload = {"product_id":123}
response = requests.get(endpoint, params=params,json=payload)
# response = requests.post(endpoint, params=params,json=payload)
# response = requests.post(endpoint, json=payload)
print(response.status_code)
print(response.text)
print(response.json())

