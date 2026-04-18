try:
	x=int(input("Enter a number: "))
	y=int(input("Enter a number: "))
	result = x/y
	print(result)
except ZeroDivisionError:
	print("denominator value should not be zero")
except ValueError:
	print("print both values should be int type")
except:
	print("Something went wrong!")
finally:
	print("Bye!!!")