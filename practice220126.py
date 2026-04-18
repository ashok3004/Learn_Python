num=int(input("Enter a  number: "))
a=0
b=1
for i in range(num):
	print(a,end=" ")
	a,b=b,a+b

'''s=input("Enter a string: ")
if s == s[::-1]:
	print("It is palindrome")
else:
	print("It is not a palindrome")
low = 0
high = len(s)-1
while low < high:
	if s[low] != s[high]:
		print("No Palindrome")
		break
		low = low + 1
		high = high -1
else:
	print("It is Palindrome")'''