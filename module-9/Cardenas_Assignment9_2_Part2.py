# Juan Cardenas
# 11/8/2026
# Module 9.2 Assignment
# Purpose: Retrieve Pokemon information using the PokeAPI

import truststore
truststore.inject_into_ssl()

import requests
import json

# Connect to the Pokemon API
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")

# Display the connection status
print("Status Code:", response.status_code)

# Check that the request was successful
if response.status_code == 200:

    # Display the unformatted API response
    print("\nUnformatted API Response:")
    print(response.text)

    # Convert the JSON response into Python data
    data = response.json()

    # Display the formatted JSON response
    print("\nFormatted JSON Response:")
    print(json.dumps(data, indent=4))

    # Display selected Pokemon information
    print("\nPokemon Information:")
    print("Name:", data["name"].capitalize())
    print("Pokemon ID:", data["id"])
    print("Height:", data["height"] / 10, "meters")
    print("Weight:", data["weight"] / 10, "kilograms")

    # Display Pokemon types
    print("\nPokemon Types:")
    for pokemon_type in data["types"]:
        print("-", pokemon_type["type"]["name"].capitalize())

    # Display Pokemon abilities
    print("\nPokemon Abilities:")
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"].capitalize())

else:
    print("Unable to retrieve Pokemon information.")