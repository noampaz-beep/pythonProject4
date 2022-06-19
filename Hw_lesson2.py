# A.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.

x = 1
y = 2

if y < x:
    print("BIG")
elif x < y:
    print("SMALL")

# B.
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.

for i in range(1, 5):
    print(i)

# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:


q = 1
if q == 1:
    print("summer")
elif q == 2:
    print("winter")
elif q == 3:
    print("fall")
elif q == 4:
    print("spring")

# D.
# 1. how many times will the following loop run?
# 2. what will be printed last?

# 1 - 10 times until count=10
# 2 - 10

# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
#
# ● Print all variables.
# ● Add the currency to your age, and check the result.

my_age = 39
print(f"my age is {my_age}")
first_letter = "P"
print(f"First letter of my last name is {first_letter}")
shekels_dollar = 3
print(f"Current shekels-dollar currency: {shekels_dollar}")
flew_abroad = True
print(f"Did I flew abroad? {flew_abroad}")
apartment_number = 20
print(f"My apartment number is {apartment_number}")
print(f"dd the currency to my age: {my_age} + {shekels_dollar} = {my_age + shekels_dollar}")

# F.
#
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the
# user entered.


phone_number = input("Please enter your phone number:")
print(f"phone number: {phone_number}")


# G.
#
# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.


def printHello():
    print("hello")


def calculate():
    sum_numbers = 5 + 3
    print(f"sum= {sum_numbers}")


# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the
# result.

def printName(name):
    print(f"my name is: {name}")


def divideByTwo(number):
    division = number / 2
    print(f"{number}/2={division}")


printName("Noam")
divideByTwo(8)


# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.

def sumOfTwo(first_num, second_num):
    return first_num + second_num


def addSpace(first_string, second_string):
    return f"{first_string} {second_string}"


# Challenges:
# K.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:

for i in range(1, 6, 1):
    result = ""
    for j in range(1, i + 1):
        result = f"{result}*"
    print(f"{result}")

# L.
# Create a nested for loop to create X shape (width is 7,
# length is 7):
for i in range(1, 8, 1):
    result = ""
    for j in range(1, 8):
        if j == i or  j== (8-i):
            result= f"{result}*"
        else:
            result = f"{result} "
    print(result)

# M.
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)

def getNum():
    number = int(input("Please enter number:"))
    sumOfTwo(number)


def sumOfTwo(number):
    if number > 9:
        my_string = str(number)
        sum_digits = 0
        for i in range(len(my_string)):
            sum_digits = sum_digits+int(my_string[i])
        print(sum_digits)


getNum()
