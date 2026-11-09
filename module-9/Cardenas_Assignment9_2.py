# Juan Cardenas
# 11/8/2026
# Module 9.2 Assignment
# Purpose: Test an API connection, and retrieve astronaut information using the OpenNotify API

import requests
import json

# Connect to the OpenNotify API
response = requests.get("http://api.open-notify.org/astros.json")

# Display the connection status
print("Status Code:", response.status_code)

# Convert the API response into Python data
data = response.json()

# Display the formatted JSON response
print("\nAstronaut API Response:")
print(json.dumps(data, indent=4))

# Display the astronaut information
print("\nAstronauts Currently in Space:")

for astronaut in data["people"]:
    print(astronaut["name"], "-", astronaut["craft"])