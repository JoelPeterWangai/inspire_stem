# Programme to calculate compound interest
# Date : 20/02/2024
# Name : Joel Peter

p = float(input("Enter principle value"))
t = float(input("Enter time in years"))
r = float (input("Enter rate  of interest"))

i = (p * (r / 100) * t)

print(" Total interest is : ", i)

a = p + i 
print("Hire purchase price is : ", a)


