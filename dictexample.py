person_info = {"name":"John","age":30,"car":None,"city": "NewYork"}
person_info.update({"age":35})
print(person_info)

'''
person_info = {"name":"John","age":30,"car":None,"city": "NewYork"}
item_list=list(person_info.items())
print(item_list)
print(type(item_list))

stud_details=['ram','sita','kumar']
course_name="python"
x=dict.fromkeys(stud_details,course_name)
print(x)

person_info = {"name":"John","age":30,"car":None,"city": "NewYork"}
for k,v in person_info.items():
	print(k,v)
k=person_info.keys()
print(k)
v=person_info.values()
print(v) '''