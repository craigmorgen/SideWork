import requests, json

quote = "Look Bruce, I\'m a part of this whether you like it not."


headers = {'Content-Type': 'application/json',
           'Cache-Control': "no-cache"}
url = "http://127.0.0.1:8080/message/new"
body = ({"message": quote})

r = requests.post(
    headers=headers,
    url=url,
    json=body
)
