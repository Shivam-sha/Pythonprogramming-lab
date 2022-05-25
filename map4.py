def square(x):
    return x*x

def cube(x):
    return x*x*x

func = (square,cube)

for i in range(8):
    val = list(map(lambda x : x(i),func))

print(val)