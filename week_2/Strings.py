# Strings in python
# Date : 22/02/2024
# Name : Joel Peter

city = "nairobi"

# Convert to uppercase

print(city)
print("\n") # prints a new line
print(city.upper())

name = "JOEL PETER"
print(name.lower())# This converts strings to lowercase

town = "       Naivasha       "

print(town)
print("\t") # new tab
print(town.strip())

f_name = "Joel"
s_name = "Peter"

full_name = f_name + s_name
print(full_name)

print(city[0]) # a
print(city[1]) # i
print(city[2])
print(city[3])
print(city[-2])
print(city[-1])
print(city[6]) # i


# Replacing a character

fruit = "orangeoooooo"

print(fruit.replace('o','Y'))

subject = "Physicsal :sciences"

print(subject.split(":"))

age = 30
height = 1.6 
print("I am {0} years old and {1} meters tall ". format(age,height))



