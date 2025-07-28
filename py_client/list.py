import requests
import json

url = "http://127.0.0.1:8000/api/product/"
response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()
# print("Data type:", type(data))           # should be <class 'dict'>
# print("Top-level keys:", data.keys())     # should show dict with 'count', 'results', etc.

# print("Paginated product list (first page):")
print(json.dumps(data, indent=2))
