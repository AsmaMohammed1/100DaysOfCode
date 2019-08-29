# Talk about String format
""" We can combine strings and numbers by using the format() method!
    The format() method takes the passed arguments, formats them,
    and places them in the string where the placeholders { } are."""

print("Welcome AS's Company")
ask = input("Enter your ID:")

Employee = "Asma Mohammed"
Emp_Num = 6
Salary = 10000
Employee1 = "Sara Ahmed"
Emp_Num1 = 5
Salary1 = 9800
Employee2 = "Huda Fahad"
Emp_Num2 = 4
Salary2 = 11000

Employee_Info ='Employee Name: {}\nEmployee Number: {}\nSalary: {}'

if ask == "6":
    print(Employee_Info.format(Employee, Emp_Num, Salary))
elif ask == "5":
	print(Employee_Info.format(Employee1, Emp_Num1, Salary1))
elif ask == "4":
	print(Employee_Info.format(Employee2, Emp_Num2, Salary2))
else:
	print("\n\tID Does'nt exist.")


# practice format with index

print('--------------------------')
name = "Asma"
print(" you're {0[0]}".format(name))

num = 2
cost = 900

print("I want {1} sunglasses from this brand and I think its cost {0}.".format(cost,num))
