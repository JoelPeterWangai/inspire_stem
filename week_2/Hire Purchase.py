# Programme to calculate hire purchase
# Date : 20/02/2024
# Name : Joel Peter

d = float(input("Enter initial deposit"))
i = float(input("Enter monthly instalment"))
t = input("Enter time in months")

h = (t * i)
print("Total monthly instalments is :", h)

a = h + d 
print("Hire purchase price is :", a)
