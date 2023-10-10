import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"

resonse = requests.get(endpoint, json={"message":"Suiii"})  #request

# print(resonse.text) # print raw text response
print(resonse.json()) # print raw json response
print(resonse.status_code)

# HTTP Request => HTML
# REST API HTTP Request => JSON
# JavaScript Object Nototion ~ Python Dict