try:
	fo=open('error.log.txt2','r')
	print(fo)
	for i in fo:
		print(i, end="")
except FileNotFoundError as e:
	print(f"{e}")
except:
	print("something went wrong")
finally:
	print("in finally block!")
	if fo:
		print("file object is closing")
	fo.close()
print("BYE!!!!!!!!!!!")