import requests
import json

url = "http://api.open-notify.org/astros.json"

# Test connection
response = requests.get(url)
print("Status Code:", response.status_code)

# Print raw response
print("\nRaw response:")
print(response.text)

# Print formatted response
print("\nFormatted response:")
data = response.json()
print(json.dumps(data, indent=4))
