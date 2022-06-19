import  requests

try:
    a=int(input("enter fist number: "))
    b=int(input("enter second number: "))
    print(a/b)
    r= open("filedffd.txt")
except ZeroDivisionError:
    print("could not divide by zero something went wrong")
except FileNotFoundError:
    print("could not find file")
print("kfdlfklds")