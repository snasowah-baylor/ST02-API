# ST02-ex01-api-github-microsoft.py

import requests

# Step 1: Call the API
url = "https://api.github.com/users/microsoft"
response = requests.get(url)


# Step 2: Convert the JSON payload to a dictionary
data = response.json()
print(data)
