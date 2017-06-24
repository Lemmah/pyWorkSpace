# This allows us to give our class attributes getters, setters and deleter attributes as is in other programming languages

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Having a function as an attribute or property using a decorator
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first.lower(), self.last.lower())

    @property
    def fullName(self):
        return "{} {}".format(self.first, self.last)

    @fullName.setter
    def fullName(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print("Deleted Name!")
        self.first = None
        self.last = None


emp1 = Employee("John", "Smith")

emp1.first = "Jim"
emp1.fullName = "James Lemayian"


print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullName)

del emp1.fullName
print(emp1.fullName)
