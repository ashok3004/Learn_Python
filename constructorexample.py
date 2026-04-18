class x:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def display(self):
		print(self.a)
		print(self.b)
	def modify(self):
		self.a=self.a+10
		self.b=self.b+10
x1=x(10,20)
x1.display()
x1.modify()
print("#"*30)
x1.display()
print("#"*30)