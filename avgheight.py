student_heights=input("input a list of students heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
total_height=0
for hight in student_heights:
    total_height += hight
print("the total hight is :",total_height)
total_students=0
for students in student_heights:
    total_students += 1
print("the no of students are :",total_students)
averge=total_height/total_students
print("the averge hight is :", averge)