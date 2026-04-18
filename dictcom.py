d1={x:x**3 for x in range(10) if x**3%4==0}
print(d1)
b = {x.upper(): x*3 for x in "python"}
print(b)
d = dict.fromkeys(range(5),True)
print(d)

'''name = ['ashok','yuthi','advi']
course = ['python','java','oracle']
d = {k:v for (k,v) in  zip(name,course)}
d1 = {k:v for (k,v) in zip(name,course)}
print(d)'''