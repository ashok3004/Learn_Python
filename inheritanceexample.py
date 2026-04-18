class x:
	def m1(self):
		self.a=100
		print("I am in m1 of x")
class y(x):
	def m2(self):
		print("i am in m2 of y")
		self.m1()
		print(self.a)
obj2=y()
obj2.m2()