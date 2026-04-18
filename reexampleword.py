import re
with open('welcome.txt','r') as fo:
	for i in fo:
		#if re.search('\w+\s\w+',i):
		if re.search('with|parot|wine',i):
			print(i)