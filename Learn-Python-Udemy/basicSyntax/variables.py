# Python variables : what is garbage collection
city = "Nairobi, Kenya"
home = "Nairobi, Kenya"

print(city)
print(home)

city = 123
home = "Good Question"

print(city)
print(home)

city = 456
print(city)

city = "Narok, Kenya"
home = city

print(city == home)
print(city is home)
