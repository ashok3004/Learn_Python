num=int(input("Eneter a number: "))
if (num<=1):
	print("this is not a prime number")
else:
	for i in range(2,num):
		if (num%i == 0):
			print("This is not a prime number")
			break
	else:
		print("it is prime number")

'''k=['a','b','c','d']
v=[10,20,30,40]
dict1={x:y for(x,y) in zip(k,v)}
print(dict1)

num=23
for i in range(2,(num//2)+1):
	if (num%i)==0:
		print(num,"is not a prime number")
		break
	else:
		print(num,"is a prime number")
else:
	print(num,"is not a prime number")


result=[p for p in range(1,11) if p%2==0]
print(result)


def find_average(name,marks):
	print(f"hi {name}")
	sum_of_marks=sum(marks)
	total_sub= len(marks)
	avg_marks=sum_of_marks/total_sub
	return avg_marks
avg_marks=find_average('siri',[75,76,89,45,46])
print(f"your avg_marks are: {avg_marks}.\f")



#### sum of this numbers #########
sum=0
print("this is progserva")
count=int(input("Enter numbers would you like to sum:"))
current_cnt=1
while current_cnt <= count:
	number=float(input("Enter a  number : "))
	sum=sum+number
	current_cnt +=1
print("sum is: ",sum)
print("The average was : ",sum/count)


mylist=[12,434,11,377,983,331]
mylist1=[12,434,11,377,983,331,"hari","nari","sai"]
for i in range(0,len(mylist)):
	for j in range(i+1,len(mylist)):
		if mylist[i] >= mylist[j]:
			mylist[i],mylist[j] = mylist[j],mylist[i]
print("sorted list",mylist)
for item in mylist1:
	if type(item) == str:
		print(item)


mylist=[10,20,30,40]
my_list1=[100,200,300,400]
for i in my_list1:
	mylist.append(i)
	print(mylist)'''