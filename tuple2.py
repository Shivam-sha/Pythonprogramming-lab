def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples, key = last)

a = [(1,3),(2,4),(3,8)]
print("sorted")
print(sort(a))