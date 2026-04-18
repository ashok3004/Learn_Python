import json
#define employee dictionary
emp_details={
	"name" : "Ashok Kumar",
	"emp_no" : 6767,
	"salary" : 5878,
	"phonenumber" : 9014374601,
	"Married" : True,
	"Children" :None
}
#Convert and write json onject to file   
with open("emp_data.json","w") as fo:
	json.dump(emp_details,fo)                      