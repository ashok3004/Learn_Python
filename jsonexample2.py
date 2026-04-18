import json
with open('data.json','r') as fo:
	data=json.load(fo)
print(type(data))