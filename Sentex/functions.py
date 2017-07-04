# Function definition in python is just by the key word def

# Unparamatized
def example_func():
    print("The example function.")

# parametarized
def simple_addition(num1, num2):
    answer = num1 + num2
    print("{} + {} = {}".format(num1, num2, answer))

# parametized with default values
def simple_add(num1=0, num2=0):
    answer = num1 + num2
    print("{} + {} = {}".format(num1, num2, answer))


simple_addition(2,3)
# you can deal with parameters indipendently with default values
simple_add(num2=4)
