import getpass
registration={"user1":{"login_name":"AK","password":"1234"},
              "user2":{"login_name":"RAJ","password":"1234"},
              "user2":{"login_name":"RAM","password":"1234"}
              }
username=input("Enter the username: ")
input_password=getpass.getpass(prompt="Enter the password: ")
for user in registration:
	if username == registration[user]["login_name"]:
		print(f"user {username} is found")
		break
	else:
		print(f"user{username} is Not found")
		exit()
	if input_password == registration[user]["password"]:
		print("password login is successful")
		break
	else:
		print("password is wrong!")
