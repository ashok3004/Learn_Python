check=lambda x: "positive" if x>0 else "negitive " if x<0 else "zero"
print(check(1))
cal=lambda x,y : (x+y,x-y,x*y,x%y)
print(cal(4,2))
a=lambda x: "Even" if x%2 == 0 else "odd"
print(a(11))