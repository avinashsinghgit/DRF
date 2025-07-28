import requests


##     ---------   GET -----------
# url = "http://127.0.0.1:8000/api/product/4/"
# response = requests.get(url=url)
# print(response.status_code)
# print(response.text)

# ##     ---------   POST -----------
url = "http://127.0.0.1:8000/api/product/create/"
body=  {"title":"To Kill a Mockingbird",
        "price":9.50}
response = requests.post(url=url, json=body)
print(response.status_code)
print(response.text)

