num=int(input("Enter a num:"))
if num>0:
	print(f"{num} is positive")
	if num<10:
		print(f"{num} is single digit")
		if num%2==0:
			print(f"{num} single digit even")
		else:
			print(f"{num} single digit odd")
	else:
		print(f"{num} is not a single digit")		
else:
	print(f"{num} is not a single digit")
print("GOOOD BYE!!!")