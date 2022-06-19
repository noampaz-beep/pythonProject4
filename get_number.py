def get_number():
    a =input("enter number")
    if a.isdecimal():
        return int(a)
    return -1
