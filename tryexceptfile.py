n=5
for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()
'''for i in range(5):
	for j in range(i):
		print("*",end=" ")
	print()

s=input("Ener a word: ")
if s==s[::-1]:
	print("It is palindrome")
else:
	print("it is not palindrome")
n=5
a,b=0,1
for i in range(n):
	print(a, end=" ")
	a,b=b,a+b


total = 0
for number in range(1,101):
	total += number
print(total)

student_marks=input("Enter the student marks: ").split()
for marks in range(0,len(student_marks)):
	student_marks[marks]=int(student_marks[marks])
	highest_score = 0
for score in student_marks:
	if score > highest_score:
		highest_score = score
print("Highest score is: ",{highest_score})


k =['a','b','c','d']
v=[10,20,30,40]
dict1={x:y for(x,y) in zip(k,v)}
print(dict1)

##listcomprehensions
prime_numbers=[num for num in range(1,101) if all(num % i != 0 for i in range(2, int(num//2) + 1))]
print(prime_numbers)

num=13
if num>1:
	for i in range(2,(num//2)+1):
		if num % i == 0:
			print("it is not a prime number")
			break
	else:
		print("it is a prime number")
else:
	print("it is not a prime number")

import random
import string
characters=string.ascii_letters+string.digits
password = ""
for i in range(8):
	password += random.choice(characters)
print(password)

try:
	fo = open('welcome22.txt','r')
	for i in fo:
		print(i,end="")
except FileNotFoundError:
	print("FileNotFound!!")
finally:
	print("In fianally Block")
	if fo:
		fo.close()
		print("file object is close")
print("\nBye!!!")'''