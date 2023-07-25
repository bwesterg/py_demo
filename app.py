# age = 20
# age = 39
# first_name = "Dude"
# is_online = False
#
# print("Hello World")
# print(age);

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)

# First: 10.1
# Second: 20
# Sum: 30.1

# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum is " + str(sum))

# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum is " + str(sum))

# calc = float(first) + float(second)
# print(calc)

# course = 'Python for noobs'
# print(course.upper())
# print(course.find('y'))
# print(course.replace('for', '4'))
# print(course)
# print('Python' in course)
# comment: prints true

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3
# comment: line 48 is equivalent to line 47.  Line 48 is called augmented assignment operator
# comment: can also use -=, *=, etc.  These are the arithmetic operators in python.

# x = (10 + 3) * 2
# print(x)

# x = 3 != 2
# print(x)

# comparison operators in python
# >
# >=
# <
# <=
# ==
# !=

# logical operators are:
# and (both), 
#or (at least one),
#not ##inverses any value given
# price = 25
# print(price > 10 and price < 30)
# print(price < 100 and price < 300)
# print(not price > 10)

#if statements
# temperature = 5

# if temperature > 30: 
#     print("It's a hot day")
#     print("drink lots of water")
# elif temperature > 20:
#     print("It's not too bad")
# elif temperature > 10:
#     print ("It's a bit cold")
# else: 
#     print("It's cold")
# print("Done")

# Weight: 170
#write function which asks a user to input weight as an integer, then asks if the units are pounds or kilograms.  It then converts pounds to kilograms, or vice versa.
weight_num = input("What is your weight? ")
unit = input("Is that number in pounds(l) or kilograms(kg)? ")
# to_pounds = weight_num * 2.2
# to_kilograms = weight_num / 2.2

if unit.upper() == "L":
    to_kilograms = float(weight_num) / 2.2
    print("Your weight is " + str(to_kilograms) + " in kilograms")
elif unit.upper() == "K":
    to_pounds = float(weight_num) * 2.2
    print("Your weight is " + str(to_pounds) + " in pounds")

print("Done")




