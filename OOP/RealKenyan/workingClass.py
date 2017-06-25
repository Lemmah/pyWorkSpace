# This is a Kenyan Citizen who is in the working class: either an employer or an employee, who generates the country some revenue

from realKenyan import KenyanCitizen


class WorkingClass(KenyanCitizen):

    # Class variables have been already inherited
    # Adding unique class variables
    PAYERate = 0.12
    totalEarnings = 0

    def __init__(self, firstName="Kenyan", lastName="Citizen", age=18, homeTown="Unknown", monthlyExpenditure=0, phoneNumber=None, monthlyEarnings=None):
        ''' Construct the working class instance variables '''
        super().__init__(firstName, lastName, age, homeTown, monthlyExpenditure, phoneNumber)
        self.monthlyEarnings = monthlyEarnings


Lemayian = WorkingClass("Regular", "Worker", 22, "Kajiado", 22000, "+254700613380")
Worker = WorkingClass.fromString("James - Lemayian - 20 - Narok - 1000 - Owns no phone")
print(Lemayian)
print(WorkingClass.totalExpenditures)
print(WorkingClass.citizenStats())
# Looking at how the inheritance flows
# help(WorkingClass)
