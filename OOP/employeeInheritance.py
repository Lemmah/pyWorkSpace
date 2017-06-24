# Inheritance allows us to inherit attributes and methods from a parent class
# We can overwrite or add completely new functionality without affecting the parent class
# Method resolution order: if a class does not have it's own constructor, the the class it inherits from constructor's used.
# Inheritance is very useful for code reuse

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


class Developer(Employee):

    raiseAmount = 1.10 # Polymorphism 'many forms'

    def __init__(self, first, last, pay, progLang):
        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.progLang = progLang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self):
        for emp in self.employees:
            print("-->",emp.fullName())







dev1 = Developer("James", "Lemayian", 50000, "Python")
dev2 = Developer("Test", "User", 89000, "Java")

mgr1 = Manager("Sue", "Smith", 90000, [dev1])

'''
print(isinstance(mgr1, Developer))
print(issubclass(Manager, Developer))

print(mgr1.email)
mgr1.addEmp(dev2)
mgr1.removeEmp(dev1)
mgr1.printEmps()

print(dev1.email)
print(dev2.email)
print(dev2.progLang)

# Apply dev's rate
print(dev1.pay)
dev1.applyRaise()
print(dev1.pay)
'''

# The help function
# help(Developer)
