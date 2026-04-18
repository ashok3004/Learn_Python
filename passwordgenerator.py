import random
import string
characters = string.ascii_letters+string.digits
password = ""
for i in range(7):
	password += random.choice(characters)
print("Your password is: ",password)
