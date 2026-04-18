guess_count=0
correct_pass='1234'
while True:
	pass_guess=input("please enter a password: ")
	guess_count +=1
	if pass_guess  == correct_pass:
		print("You have login succefully")
		break
	elif pass_guess != correct_pass:
		if guess_count >=3:
			print("You have reached 3 time wrong password ")
			print("Your account is locked!!")
			break


'''i=0
while i<=10:
	i+=1
	if i==5 or i==8:
		continue
	print(i)


b=int(input("please enter a table number: "))
i=1
while i<=10:
	print(b,'X',i ,'=' , b*i)
	i+=1
	'''