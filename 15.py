def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age cannot be negative")


try:
    get_age()
except ValueError as e:
    print(e.args)


a = input("enter number: ")
def check_my_number(num):
    a = ""
    try:
        a=(num)
    except ValueError:
        return False
    if str(num).isdecimal() or str(num).isdigit():
        print("ddd")