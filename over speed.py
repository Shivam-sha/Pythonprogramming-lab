d =  int(input("enter the distance"))
t = int(input("enter the time"))
speed = d//t
for i in speed:
    if i>=50:
        print("overspeed")

print(speed)