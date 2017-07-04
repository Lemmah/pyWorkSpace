# tuple is immutable => you cant change stuff here
# list is mutable => you can manipulate it, change values
# remove stuff from it

x = 2,5,6 # is a tuple
x = (2,5,6)

y = [2,5,6]

def example_func():
    return 5,6

# tuples used in variable sequence unpacking
x,y = example_func()
