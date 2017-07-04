
x = [1,2,3,4,5,6,7,8,9]
print(x)
x.append(23)
print(x)
x.insert(2,99)
print(x)
x.remove(2)
print(x)
x.remove(x[2])
print(x)

# slicing data
print(x[3:7])
print(x[-2:])

# finding the index
print(x.index(8))

# counting elements
print(x.count(5))

# sorting
x.sort()
print(x)
