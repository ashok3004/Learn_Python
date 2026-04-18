correct_pin=1234
max_attepts=3
attepts=0
while attepts<max_attepts:
	entered_pin=input("Please enter the pin: ")
	if entered_pin == correct_pin:
		print("Pin acceepted ! and You have succcessfully logged in!")
		break
	else:
		attepts+=1
		print(f"Incorrect pin ,you {max_attepts - attepts} attepts left")
    if attepts == max_attepts:
    	print("Too many incorrect logins attempts.your account is now blocked!")