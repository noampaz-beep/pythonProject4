isTrue = False
a=2
b=2
strOne = "One"
strThree = "Three"
c=[1.2,3]
d=[1,2,3]
print(type(a))
if type(a) is int:
    print("a equals b")

if a==b:
    print("a equals b")
if c==d:
    print("c equals d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")


age = int(input("enter your age:"))
if 0 <age <120:
    print("ok")


my_names = ["adi","ben","noam","arthur","ron"]
my_list = []

if my_list:
    print("my list is not empty")
if my_names:
    print("my list is not empty")
if len(my_names)>0:
    print("length greater than 0")

if "zohar" in my_names:
    print("i found Zohar")
elif "zohar" not in my_names:
    print("no Zohar")


if a < b and (strThree == 3 or isTrue ==4):
    print("a is less than b")
elif a==b:
    print("a is equal b")
else:
    print("a is greater than b")