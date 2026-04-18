try:
	x=int(input("Enter a numnber: "))
	y=int(input("Enter a number: " ))
	result=x/y
	print(result)
except ZeroDivisionError as e:
	print(f"some thing went wrong",{e})
except ValueError as e:
	print(f"both value should be integer")
else:
	print("the operation was successful")
print("bye")