# A blue print of a Kenyan Citizen. The common categories.
# Citizen, WorkingClass, Unemployed.
# WorkingClass => Employer, Employee.

class KenyanCitizen:
    ''' A blue print of the Kenyan citizen '''

    # 1.0: Class variables => may not affect the instances directly but have a logical connection
    valueAddedTax = 0.16
    genRevenue = 0 # => the revenue an individual generates for spending
    nationality = "Kenyan"

    ## Collect age statistics
    youth = 0
    middleAge = 0
    old = 0

    # Collect expenditure statistics
    # Country expenditure is calculated here in a citizens class because I think there is a logical connection
    # between the citizen's expenditure and the country's total expenditure
    countryExpenditure = 0

    def __init__(self, firstName="Kenyan", lastName="Citizen", age=18, homeTown="Unknown", monthlyExpenditure=0, phoneNumber=None):
        ''' Constructing the Kenyan Citizen '''
        # 1.1 Instance variables: properties of the specific instance of the Kenyan citizen
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.homeTown = homeTown
        self.monthlyExpenditure = monthlyExpenditure
        # People consider their phoneNumbers private
        self.__phoneNumber = phoneNumber

        # Update age statistics on every instance
        if self.age < 30:
            KenyanCitizen.youth += 1
        elif self.age < 50:
            KenyanCitizen.middleAge += 1
        else:
            KenyanCitizen.old += 1

        # Update country expenditure
        KenyanCitizen.countryExpenditure += monthlyExpenditure


    @property
    def fullName(self):
        ''' The full name property getter '''
        return "{} {}".format(self.firstName, self.lastName)

    @fullName.setter
    def fullName(self, newName):
        ''' Reseting the names using the full name '''
        self.firstName, self.lastName = newName.split(" ")

    @fullName.deleter
    def fullName(self):
        ''' Deleting the names using full name property '''
        print("Deleted the name!")
        self.firstName, self.lastName = None, None

    @property
    def phoneNum(self):
        ''' The phone number property getter '''
        if self.__phoneNumber is None:
            return "Owns no phone"
        return self.__phoneNumber

    @phoneNum.setter
    def phoneNum(self, phoneNumber):
        ''' Setting a citizen's phone number '''
        self.__phoneNumber = phoneNumber

    @phoneNum.deleter
    def phoneNum(self):
        ''' Deleting the phone number propery. '''
        self.__phoneNumber = None

    def calcMonthlyTax(self):
        ''' Calculating the monthly tax revenue for citizen instance '''
        self.genRevenue = self.monthlyExpenditure * valueAddedTax
        return self.genRevenue

    # 2.0: Class methods => manipulating my class variables to achieve desired effects
    @classmethod
    def citizenStats(cls):
        ''' Formating and returning the citizen stats '''
        return "Young: {}\nMiddle aged: {}\nOld people: {}\n".format(cls.youth, cls.middleAge, cls.old)

    @classmethod
    def averageSpend(cls):
        ''' Getting the average's Kenyan Citizen's spending '''
        return cls.countryExpenditure / (cls.youth + cls.middleAge + cls.old)

    @classmethod
    def fromString(cls, useString):
        ''' Alternative constructor from string '''
        firstName, lastName, age, homeTown, monthlyExpenditure, phoneNum = useString.split(" - ")
        if phoneNum == "Owns no phone":
            phoneNum = None
        return cls(firstName, lastName, int(age), homeTown, int(monthlyExpenditure), phoneNum)

    # 3.0: My special dunder methods
    def __repr__(self):
        ''' A friendlier representation of the Kenyan citizen object instance. '''
        if self.__phoneNumber is not None:
            return "KenyanCitizen('{}', '{}', {}, '{}', {}, '{}')".format(self.firstName, self.lastName, self.age, self.homeTown, self.monthlyExpenditure, self.__phoneNumber)
        return "KenyanCitizen('{}', '{}', {}, '{}', {}, {})".format(self.firstName, self.lastName, self.age, self.homeTown, self.monthlyExpenditure, self.__phoneNumber)

    def __str__(self):
        ''' An end-user representation of the Kenyan citizen object instance. '''
        return "{} - {} - {} - {} - {} - {}".format(self.firstName, self.lastName, self.age, self.homeTown, self.monthlyExpenditure, self.phoneNum)


Lemayian = KenyanCitizen.fromString("James - Lemayian - 20 - Narok - 1000 - Owns no phone")
SomeOldCitizen = KenyanCitizen("FatherOf", "Many", 55, "Nairobi", 20000)
print(KenyanCitizen.countryExpenditure)
print(KenyanCitizen.averageSpend())
'''
print(KenyanCitizen.citizenStats())
print(Lemayian.phoneNum)
Lemayian.phoneNum = "0700613380"
print(Lemayian.phoneNum)

del Lemayian.phoneNum
print(Lemayian.phoneNum)
print(Lemayian)
print(KenyanCitizen("James", "Nakolah", 23, "Nairobi", 2323, None))
'''
