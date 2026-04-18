class bankapp:
	bank_name="ICIC"
	def __init__(self,cname,cadd,caccnum,cbal):
		self.cname=cname
		self.cadd=cadd
		self.caccnum=caccnum
		self.cbal=cbal
	def deposit(self,depamt):
		self.cbal=self.cbal+depamt
	def withdraw(self,wamt):
		if wamt < self.cbal:
			self.cbal=self.cbal-wamt
		else:
			print(f"insufficent funds.your current Available balence is:{self.cbal} but you are trying to withdraw for {wamt}")

	def display(self):
		print(f"Hi {self.cname}")
		print(f"Thank you for using {bankapp.bank_name}")
		print(f"Current Availble balence is: {self.cbal}")
cust1=bankapp('Ashok','Nizamabad',1122014094040,21000)
cust1.deposit(2000)
cust1.display()
cust1.withdraw(54000)
cust1.display()
