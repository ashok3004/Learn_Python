def addition(a,b):
	print(a+b)
def smart_dec(func):
	def inner(a,b):
		return func(a,b)
	return inner
add=smart_dec(addition)
add(45,45)
addition(20,25)