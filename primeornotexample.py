correct_pin="1234"
gues_count=0

while True:
	pass_guess=input("please enter your password: ")
	gues_count +=1
	if pass_guess == correct_pin:
		print("you have logged in successfuly")
		break
	elif pass_guess !=correct_pin:
		if gues_count>=3:
			print("you entered 3 times limit")
			print("you have been denied")
			break





'''corect_pass=1234
attemts=0:
while True:
	enter_pin=iput("Enter a pin")
if enter_pin == corect_pass:
	print("you have logged succesfully")
	break
elif:
	print("you have wrong password!!!")



num=int(input("Enter a number : "))
def is_prime(n):
	if n<2:
		return False
	return all()

num=int(input("Enter a number : "))
if num==0 or num==1:
	print("The given number is not prime number")
elif num>1:
	for i in range(2,num):
		if(num % i == 0):
			print(num,"it is not a prime number")
			break
	else:
		print(num,"it is a prime number") '''