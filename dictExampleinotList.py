#converting the dictionary into the list
emp={101:"sam",102:"ram",103:"john"}
my_emp2={104:"arun",105:"ashok",106:"aasy"}
print(type(emp))
x=list(emp.items())
print(x)
print(type(x))
key_list=list(emp.keys())
print(key_list)
key_values=list(emp.values())
print(key_values)
emp.update(my_emp2)
print(emp)