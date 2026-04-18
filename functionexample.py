'''
#find the averge of students
def find_avg_marks(name,marks):
	print(f"Hi {name} is ")
	sum_of_marks=sum(marks)
	total_sub=len(marks)
	avg_marks=sum_of_marks/total_sub
	return avg_marks
def compute_grade(avg_marks):
	if avg_marks >=70:
		grade = 'A'
	elif avg_marks >=60 and avg_marks<=69:
		grade = 'B'
	elif avg_marks >=45 and avg_marks<=59:
		grade = 'C'
	else:
		grade = "Fail"
	return grade
avg_marks=find_avg_marks('siri',[78,65,53,75,71])
print(f"your avg_marks are: {avg_marks}")
compute_grade(avg_marks)
result = compute_grade(avg_marks)
print(f"your grade is :",result)


def test(a,b):
	if a>b:
		return a
	else:
		return b
print("Highest value is: ",test(10,20))
#without return
def add(a,b):
	x=a+b
print(add(22,33))

def add(a,b):
	x=a+b
	return x


def add(a,b):
	x=a+b
	return x
add(10,20)
print(add(11,20))



def cal(x,y):
	print(f"sum of {x} and {y} is: {x+y}")
	print(f"div of {x} and {y} is: {x-y}")
	print(f"mul of {x} and {y} is: {x*y}")
	print(f"div of {x} and {y} is: {x%y}")
cal(10,4)



def f1(x,y):
	print("I am in f1")
	print(x)
	print(y)
f1(20,30)'''