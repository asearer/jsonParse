import json

# Example JSON data
json_data = '''
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "features": {
    "height": 180,
    "weight": 75
  },
  "languages": ["Python", "JavaScript", "Java"]
}
'''

# Load the JSON data
data = json.loads(json_data)

# Access the relevant data
name = data["name"]
age = data["age"]
city = data["city"]
height = data["features"]["height"]
weight = data["features"]["weight"]
languages = data["languages"]

# Print the extracted data
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Height:", height)
print("Weight:", weight)
print("Languages:", languages)
