a = set([10,20,30,40,50])
b = set([10,60,70])
print(a)
print(a.intersection(b))
print(a.difference(b))
print(a.union(b))

print(b.intersection(a))
print(b.difference(a))
print(a.union(b))