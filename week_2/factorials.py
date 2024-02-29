# Programme to calculate factorials
# Date : 20/02/2024
# Name : Joel Peter

num = int(input("Enter a number to find a factorial: "))
count = 1
for i in range(1,num+1):
    count *= i

print(count)


factorial_numbs = 1
max_value = int(input("Enter maximum value"))
for x in range(1,max_value+1):

    factorial_numbs = factorial_numbs * x

print(factorial_numbs)

#Printing odd numbers
for i in range (1,20,2):
    print(i)

#Printing even numbers
for i in range (0,20,2):
    print(i)

