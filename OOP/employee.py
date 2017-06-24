# Employee blue print
# Every method in a class takes the instance as the first argument
# Self is the instance that works with all instances

class Employee:
    ''' This is the class that has employee attributes and behaviors '''

    # Class variables
    raiseAmount = 1.04
    numOfEmployees = 0

    def __init__(self, first, last, pay):
        ''' The constructor, special init method. Self is the instance by convenction. These are set across any instance of Employee '''
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@company.com"

        Employee.numOfEmployees += 1

    def fullName(self):
        ''' This is the full name property method. '''
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)


print(Employee.numOfEmployees)

emp_1 = Employee("James", "Lemayian", 40000)

print(emp_1.email) # in the class it's emp_1.email => self.email

print(Employee.fullName(emp_1))
print(emp_1.fullName()) # This passes the instance automatically.


print(Employee.numOfEmployees)
#print(emp_1.pay)
#emp_1.applyRaise()
#print(emp_1.pay)

# Looking at class variables
# print(Employee.raiseAmount)
# print(emp_1.raiseAmount)

# Printing namespaces
# print(emp_1.__dict__)
# print(Employee.__dict__)
