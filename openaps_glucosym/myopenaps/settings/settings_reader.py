import json

with open("settings.json") as settings_data:
	data = json.load(settings_data)
	print(data[0])
