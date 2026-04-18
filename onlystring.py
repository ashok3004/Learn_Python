mylist=[10,20,30,40,50,"python","unix","shell",101,202]
strings_only=[]
for i in mylist:
	if isinstance(i,str):
		strings_only.append(i)
print(strings_only)
