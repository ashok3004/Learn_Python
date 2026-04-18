import json
with open('example.json','r') as file:
	data_dict=json.load(file)
print(data_dict)
print(type(data_dict))