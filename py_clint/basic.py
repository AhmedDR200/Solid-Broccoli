import requests


endpoint = "http://localhost:8000/api/"

resonse = requests.get(endpoint,params={"abc":123}, json={"message":"Suiii"})  #request

print(resonse.text) # print raw text response
print(resonse.json()) # print raw json response
print(resonse.status_code)

# HTTP Request => HTML
# REST API HTTP Request => JSON
# JavaScript Object Nototion ~ Python Dict