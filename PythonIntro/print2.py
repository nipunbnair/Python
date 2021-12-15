a = [5, 10, 15, 20, 25, 30, 35, 40]
a[2] = 43
print(a[2])
print(a[0:3])
print(a[5:])
print(a[:5])
name = ["Amma", "Tripty", "Amrita"]
for i in range(len(name)):
    print("i like", name[i])

k = 1
print(type(k))
k = 'a'
print(type(k))
k = 2.0
print(type(k))
k = 1 + 2j
print(isinstance(1 + 2j, complex))
