#Discount caluclation
is_member=True
has_coupon=True
purchase_amount=int(input("Enter a purchase amount:"))
if purchase_amount>1000:
	if is_member:
		if has_coupon:
			print("You get 30% discount")
		else:
			print("you get a 20% discount")
	else:
		print("you get a 5% discount")
else:
	print("No Discount provided")