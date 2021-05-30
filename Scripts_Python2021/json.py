import json
content = {}

with open('MusicCollection.json') as file_json:
    content = json.loads(file_json)

print(content)   