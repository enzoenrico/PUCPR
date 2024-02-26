import requests

uri = "http://localhost:3000/api"

payload = {"posX":"testepy", "posY":"TestePy"}

req = requests.get(uri)

print(req.json)