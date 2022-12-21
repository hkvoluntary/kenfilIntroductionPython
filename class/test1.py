var1 = [10,20]
var2 = var1
var3 = var1
print(var1)
print(var2)
print(var3)

var1.append(30)
print(var1)
print(var2)
print(var3)

var1 = "hello"

print(var1)
print(var2)
print(var3)

print(id(var1))
print(id(var2))
print(id(var3))

var2 = var1

print(var1)
print(var2)
print(var3)

print(id(var1))
print(id(var2))
print(id(var3))
