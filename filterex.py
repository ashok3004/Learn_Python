L = ["apple", "", None, "banana", 0, "cherry"]
b = filter(None,L)
print(list(b))
'''li=["banana","apple","avacado","appricot","cherry","jama","kiwi"]
a = filter(lambda w:len(w)>5,li)
print(list(a))

li=['banana','apple','avacado','appricot','cherry']
def start_a(w):
	return w.startswith("a")
res=(filter(start_a,li))
print(list(res))
'''