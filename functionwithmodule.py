x=100
def f1():
	print("I am in f1")
	print(x)
def f2():
	print("I am in f2")
	print(x)
	a=11
	print(a)
def add(a,b):
	x=a+b
	return x
	#print(f"the addition of a,b : {x}")

f1()
f2()
print(add(12,12))
print("outside")
print(x)