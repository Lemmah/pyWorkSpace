# Employee blue print
# Every method in a class takes the instance as the first argument
# Self is the instance that works with all instances
# Regular methods take the instance as the first argument
# Class methods take the class as the first argument
# Class methods can be used as alternative constructors
# Static methods dont pass anything as the first argument, they are just any other functions included in the classes because they have a logical connection to our classes but do not actually depend on any specific instance.
# If you're not using the class or instance in your function, then it is a good candidate for a static function

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

    @classmethod
    def setRaiseAmt(cls, amount):
        cls.raiseAmount = amount

    # Alternative constructor for a different usecase
    @classmethod
    def fromString(cls, empString):
        first, last, pay = empString.split("-")
        return cls(first, last, pay)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



# Static Method
import datetime
myDate = datetime.date(2017, 7, 12)
print(Employee.isWorkDay(myDate))


# Special use cases
empString1 = "John-Doe-70000"
empString2 = "Steve-Smith-3000"
empString3 = "Jane-Doe-20000"

# Using alternative constructors
newEmployee1 = Employee.fromString(empString1)
newEmployee2 = Employee.fromString(empString2)

print(newEmployee1.fullName())

print(Employee.numOfEmployees)

emp_1 = Employee("James", "Lemayian", 40000)

print(emp_1.email) # in the class it's emp_1.email => self.email

print(Employee.fullName(emp_1))
print(emp_1.fullName()) # This passes the instance automatically.


print(Employee.numOfEmployees)
#print(emp_1.pay)
#emp_1.applyRaise()
#print(emp_1.pay)

# Looking at class variables and class methods
Employee.setRaiseAmt(1.05) # => class method
print(Employee.raiseAmount) # => class variable
print(emp_1.raiseAmount)

# Printing namespaces
# print(emp_1.__dict__)
# print(Employee.__dict__)
