# Buzzword: operator overloading
# Double underscore: dunder

# Special methods are also called magic dunder methods.
# Special methods allow us to emulate some built-in behaviours in python
# These are what allow us to implement operator overloading
# Special methods are surrounded by dunders


class Employee:

    raiseAmount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.pay = pay

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

    # Good to have this is a default
    # We are trying to return a developer friendly way of recreating the object
    def __repr__(self):
        return "Employee('{}','{}', '{}')".format(self.first, self.last, self.pay)

    # Meant to be more readable for the end user
    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

    # Manipulating how we add our employees
    def __add__(self, other):
        return self.pay + other.pay

    # Maybe we want to return the length of employees full name
    def __len__(self):
        return len(self.fullName())

emp1 = Employee("James", "Lemayian", 34000)
emp2 = Employee("Test", "User", 34000)

print(emp1) # => runs __str__ by default if available
print(repr(emp1)) # => explicitly run the __repr__ method
print(str(emp1)) # => explicity run the __str__ method

# Defined magic addition dunder
# Like how do we add objects of our own types
print(emp1 + emp2)

# What about the length of an employees fullName
print(len(emp1))
print(len(emp1.fullName()))
