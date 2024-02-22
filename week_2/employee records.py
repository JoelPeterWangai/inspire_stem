# This is a programme to show employee records
# Date :20/02/2024
# Name : Joel Peter

name = input("Enter name of employee :")
age = input("Enter age of employee :")
salary = int(input("Enter salary of employee :"))
bonus = int(input("Enter employee bonus"))

inc = 130/100 
increased_salary = (salary * inc)
print("The increased salary is : ", increased_salary)

dec = 5000
new_bonus = (bonus - dec)
print("New bonus is : ", new_bonus)
