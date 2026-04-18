import re
s = "abaya"
fist = re.findall(r'^([a-z])',s)
last = re.findall(r'([a-z])$',s)
if fist and last and fist[0] == last [0]:
	print("valid")
else:
	print("invalid")