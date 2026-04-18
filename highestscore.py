student_marks=input("input a list of student marks: ").split()
for marks in range(0,len(student_marks)):
    student_marks[marks]=int(student_marks[marks])
print(student_marks)
highest_score=0
for score in student_marks:
    if score > highest_score:
        highest_score= score
print("The highest score is : ",{highest_score})