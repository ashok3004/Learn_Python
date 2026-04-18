import json
#jsonstring='{"id":121,"name":"Ashok","course":"Java","Married":true,"children":null}'
#print(type(jsonstring))
#stud_details=json.loads(jsonstring)
#print(type(stud_details))
with open('data.json','r') as fo:
	data=json.load(fo)
print(data)