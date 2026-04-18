#Have at least one number
#Have at least one uppercase letter
#Have at least one lowercase letter
#Have at least one special character ($, @, #, %)
#Be between 6 and 20 characters in length
import re
s="Abaced1"
if len(s)>=6 and len(s)<=20:
	if re.findall('[a-z]',s) and re.findall('[A-Z]',s) and re.findall('[0-9]',s) and re.findall('[$@#%]',s):
		print(" The given password is valid")
	else:
		print(" Invalid Passoword!!")
else:
	print("Invalid Password!!")