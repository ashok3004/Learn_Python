mylist=[10,20,30,40,31,50]
for i in range(0,len(mylist)):
	for j in range(i+1,len(mylist)):
		if mylist[i] >= mylist[j]:
			mylist[i],mylist[j]=mylist[j],mylist[i]
print("sorted list is",mylist)


'''mylist=[10,20,30,40,'hi','hello','john','anil',50]
for item in mylist:
	if type(item) == str:
		print(item)
print(mylist.count(30))
print(mylist.index(30))
mylist.insert(3,'python')
print(len(mylist))
print(mylist)


mylist=[10,20,30,40]
mylist2=[50,60,70,80]
mylist.extend(mylist2)
print(mylist) '''