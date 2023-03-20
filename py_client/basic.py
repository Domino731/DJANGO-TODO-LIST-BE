import requests

endpoint = 'http://localhost:8000/api/'

request = requests.get(endpoint, json={"title": "Hello World!!!"})

print('API JSON: ', request)
