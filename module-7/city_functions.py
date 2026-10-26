# Juan Cardenas
# 10/25/2026
# Module 7.2 Assignment
# Purpose: To write a Python program that formats city and country names.
# Then create tests at the function level to make sure my code works as expected.

def city_country(city, country, population=None, language=None):
    """Return a city and country with optional population and language."""
    location = f"{city}, {country}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language}"

    return location

# Call the function using different combinations of arguments.
print(city_country("Berlin", "Germany"))
print(city_country("Paris", "France", 2100000))
print(city_country("Tokyo", "Japan", 14000000, "Japanese"))