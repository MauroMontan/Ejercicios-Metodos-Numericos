import requests
import json
  
reqUrl = "https://16me0w.deta.dev/recipies/"

headersList = {
    "Content-Type": "application/json"
}
  

payload = {
    "key": "string",
    "recipie_name": "string",
    "author": "string",
    "cook_time": "string",
    "prepare_time": "string",
    "ingredients": "string",
    "directions": "string",
    "card_color": "string"
}

response = requests.request("POST", reqUrl, data=json.dumps(payload),  headers=headersList)

print(response.text)
