# A blue print of a Kenyan Citizen. The common categories.
# Citizen, WorkingClass, Unemployed.
# WorkingClass => Employer, Employee.

class KenyanCitizen:

    valueAddedTax = 0.16
    genRevenue = 0 # => the revenue an individual generates for spending
    nationality = "Kenyan"

    ## Collect age statistics
    youth = 0
    middleAge = 0
    old = 0

    def __init__(self, firstName="Kenyan", lastName="Citizen", age=18, homeTown="Unknown", monthlyExpenditure=0):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.homeTown = homeTown
        self.monthlyExpenditure = monthlyExpenditure

        # Update age statistics on every instance
        if self.age < 30:
            KenyanCitizen.youth += 1
        elif self.age < 50:
            KenyanCitizen.middleAge += 1
        else:
            KenyanCitizen.old += 1

    @property
    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)

    @fullName.setter
    def fullName(self, newName):
        self.firstName, self.lastName = newName.split(" ")

    @fullName.deleter
    def fullName(self):
        print("Deleted the name!")
        self.firstName, self.lastName = None, None

    def calcMonthlyTax(self):
        self.genRevenue = self.monthlyExpenditure * valueAddedTax
        return self.genRevenue

    @classmethod
    def citizenStats(cls):
        return "Young: {}\nMiddle aged: {}\nOld people: {}\n".format(cls.youth, cls.middleAge, cls.old)


Lemayian = KenyanCitizen("James", "Lemayian", 20, "Narok", 1000)
SomeOldCitizen = KenyanCitizen("FatherOf", "Many", 55, "Nairobi", 20000)
print(KenyanCitizen.citizenStats())
