######### python object serializaton ####
#### json file to python dictionary####json.load()###
import json
jsonstring='{"name":"John", "age":30, "car":null}'
with open('emp_data.json') as fo:
	data=json.load(fo)
print(data)
print(type(data))

'''###### json strings  to python dictionary ====> json.loads()###
import json
json_string='{"name":"John", "age":30, "car":null}'
print(type(json_string))
stud_details=json.loads(json_string)
print(stud_details)
print(type(stud_details))


####### file found or not ###########
try:
	fo=open('welcome2.txt')
	print(fo)
	for i in fo:
		print(i,end="")
except FileNotFoundError:
	print("file not found ")
except:
	print("something went wrong")
finally:
	print("finally block")
if fo:
	print("file object is closed")
	fo.close()
###### Exception Handling (compileerrors--> syntax,indenation errors AND run time errors -->type/value..etc errors) #####
try:
	x=int(input("Enter a num1:"))
	y=int(input("Enter a num2:"))
	result=x/y
	print(result)
except ZeroDivisionError:
	print("denominator vallue shold not be zero")
except ValueError:
	print("both input should be int type")
except:
	print("something went wrong")
print("Bye")


### REG mobile number validation##############
import re
with open('welcome2.txt','r') as fo:
	for i in fo:
		if re.search('[0-9]{10}',i):
			print(i,end=" ")




############# REG Expression ###############
import re
with open('welcome.txt','r') as fo:
	for i in fo:
		x2=re.sub('asho','python',i)
		print(x2,end="")


##### search operation ############
import re
with open('welcome.txt','r') as fo:
	for i in fo:
		if re.search('asho',i):
			print(i,end="")


##########File handling###################


#write data with w+ #####
fo=open('welcome3.txt','w+')
fo.write("Welcome to the python\nAsnible\njava\n")
fo.seek(0) # offset is the number of bytes to move the file pointer 0-> begining of the file
k1=fo.readlines()
print(k1)
print("curren cursor position is: ",fo.tell())
fo.close()
#write data#####
fo=open('welcome2.txt','w')
fo.write("Welcome to the python")
k1=fo.read()
print(k1)
Note: io.UnsupportedOperation: not readable

#readlines
fo=open('welcome.txt')
k=fo.readlines()
for i in k:
	print(i, end="")
fo.close()
###############read########
fo=open('welcome.txt')
x=fo.read()
print(x)
print(type(x))

####################################################3
my_dict={'a':1,'b':2,'c':3}
item_list=list(my_dict.items())
print(item_list)
#my_dict.update({'c':5})
for key in my_dict:
	if key=='c':
		my_dict[key]=7
print(my_dict)

##########################################################################
emp_details={101:"john",102:"ram",103:"siri",105:["ashok","devops","us"]}
student_details={'ram','sita','bob'}
course_name='python'
print(emp_details)
print(emp_details[102])
print(emp_details[105][2])
print(emp_details.keys())
print(emp_details.values())
x=dict.fromkeys(student_details,course_name	)
print(x)


person_info={"name":"John","age":30,"car":None}
print(person_info['name'])
print(person_info.get('age'))
print('agee' in person_info)
#################################################################################
mylist=[10,20,30,40,100,110,140,45,76,31]
print(mylist[-1])
x=sorted(mylist)
print(x)
print(mylist)
print(mylist.index(40))
to get the only strings in the list
my_list=[10,20,30,40,'siri','giri','liri',88,99,'asay',111,True]
print(my_list)
for item in my_list:
	if type(item) == str and type(item) == bool:
		print(item)



guess_count=0
correct_pass='1234'
while True:
	pass_guess=input("Enter the password: ")
	guess_count+=1
	if pass_guess==correct_pass:
		print("You have successfully logged in")
		break
	elif pass_guess!=correct_pass:
		if guess_count>=3:
			print("You have entered 3 times limit crossed!")
			print("You have been denied access")
			exit()

#keeps asking for numbers until count have been entered
#Prints the average value
sum=0
print("This program will take sevaral numbers,then average them.")
count=int(input("How many numbers would you like to sum: "))
current_count=1
while current_count <=count:
	print("Number",current_count)
	number=float(input("Enter a number: "))
	sum=sum+number
	current_count +=1
print("sum is:",sum)
print("The average was:",sum/count)


i=1
while True:
	print(i,"Hello")
	if i==10:
		break
	i+=1
######################
i=1
while i<=10:
	print(i)
	i+=1
###########################
for i in range(1,51):
	if i%3==0 and i%5==0:
		print("FizzBuzz")
	elif i%3==0:
		print("Fizz")
	elif i%5==0:
		print("Buzz")
	else:
		print(i)'''
