# Programme to solve quadratic equations
# Date : 20/02/2024
# Name : Joel Peter

a =float (input(" eneter coefficient of first term: "))
b = float(input (" eneter coefficient of second term: "))
c =float( input("enter constant: "))

d = float((float(b)**2) - 4 * float(a) * float(c))

x_1 =( (-b +  math.sqrt(d)) / 2 * a)
x_2 =( (-b -  math.sqrt(d)) / 2 * a)

print("The solution of the quadratic equation is :", x_1)
print("The solution of the quadratic equation is :", x_2)



