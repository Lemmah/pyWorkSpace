# Variable rules

import keyword
for keyword in keyword.kwlist:
    print(keyword, end = ", ")

# Define and assign multiple variables to the same value

a = b = c = 100
print(a,b,c)

x, y, z = 10, 20, 30
print(x,y,z)
