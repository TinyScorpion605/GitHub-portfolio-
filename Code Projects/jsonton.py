import json

with open('city.json') as file:
    json.load(file)

print(file['name'])
