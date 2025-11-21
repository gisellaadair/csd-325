import requests
import json  # if needed for formatting

# endpoint from tutorial
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print("Status Code:", response.status_code)
data = response.json()
print(json.dumps(data, indent=4))  # pretty print
