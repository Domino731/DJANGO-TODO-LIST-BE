import requests

get_response = requests.get('http://localhost:8000/', params={"abc": "abc"}, json={"data": "HELLO WORLD"})
print(get_response.json())
