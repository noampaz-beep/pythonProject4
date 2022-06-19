a="hello world"
my_names = ["adi","ben","noam","arthur","ron"]
print(list(range(1,10,3)))
for i in range(1,6):
    print(f"hello world #{i}")

for name in my_names:
    print((f"hello {name}"))
    if name == "arthur":
        break
else:
    print("printed all names")

for i in range(len(my_names)):
    print(my_names[i])

a=0
while a<5:
    print(a)
    a=a+1
    if a==2:
        continue
    break
    a=a+1

l=[]
current_input=input("enter letter:")
while current_input !="q":
    l.append(current_input)
    current_input=input("enter letter: ")

print(l)

n=[1,2,3,4,5]
result= []
## way 1
for num in n:
    result.append(num*2)
## way 2 : loop in single line
result= [num *2 for num in n if num>2]

