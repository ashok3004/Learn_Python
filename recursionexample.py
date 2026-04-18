def fibonaci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonaci(n-1)+fibonaci(n-2)
print(fibonaci(10))


'''def factorial(n):
	if n == 0 :
		return 1
	else:
		return n *factorial(n-1)

print(factorial(5))
'''