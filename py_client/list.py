import requests

url = "http://127.0.0.1:8000/api/product/4"
response = requests.get(url=url)
print(response.status_code)
print(response.text)

