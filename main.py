import requests, json


desc = "You did it!"


headers = {'Content-Type': 'application/json'}
url = "http://127.0.0.1:8080/message/new"
body = ({'message': desc})

r = requests.post(
    headers=headers,
    url=url,
    json=body
)

print(body)
