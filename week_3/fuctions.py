# Functions are  block of code runnning  together as a unit
# eg sum(10,20) 10 and 20 are the parameters of the function

# We first initialie the function then we call the funcion

# Initializing uses a key word (def)

# There are two types of functions: 1. User defined 2. Built in

#HOW TO DEFINE A FUNCTION
def print_name():
    print("My name is Joel Peter")

#Calling the function
print_name()
print_name()
print_name()
print_name()
print_name()


def print_details(name , age , ID , gender):
    print(" I am {0} , I am {1} , My ID no is {2} , I am {3}".format(name , age , ID , gender))


print_details("Joel Peter" , "18" , "13446244513" , "Male")
print_details("Lucy Wanjiku" , "18" , "13446244353" , "Female")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

def prod_nums(m,n):
    return m * n

print(prod_nums(3,4))

# HOW TO USE FOR LOP INSIDE  FUNCTION
def print_odds(first_num,last_num):
    for i in range(first_num,last_num):
        print(i %2)

print_odds(0,15)


