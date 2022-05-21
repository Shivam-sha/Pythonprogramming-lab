# python program to find the number of vobels

v = input("enter the character")
if v.lower() in ("a","e","i","o","u"):
    print("vobel")
elif v.upper() in ("A","E","I","O","U"):
    print("vobel")
else:
    print("constant")
    