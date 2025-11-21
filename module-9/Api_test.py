import requests

# Test connection
response = requests.get('http://www.google.com')
print("Status Code:", response.status_code)
