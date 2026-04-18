import random
names=["ashok","kumar","chakram","micky","mimmy"]
num_items=len(names)
ramdom_choice=random.randint(0,num_items-1)
person_who_pay=names[ramdom_choice]
print(person_who_pay+" is going to buy the meal today")