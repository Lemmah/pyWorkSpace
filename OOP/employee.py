# Employee blue print
# Self is the instance

class Employee:
    ''' This is the class that has employee attributes and behaviors '''
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        ''' This is the full name property method. '''
        return "{} {}".format(self.first, self.last)




emp_1 = Employee("James", "Lemayian", 40000)

print(emp_1.email)
print(emp_1.fullName())
