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

    # Operator overloading in practice
    def __add__(self, other):
        ''' Get the net earnings of two employees by simply adding them together '''
        if self.monthlyEarnings is not None and other.monthlyEarnings is not None:
            return self.monthlyEarnings + other.monthlyEarnings
        else:
            return "One of them doesn't earn."

# This will only get to run if this is the file being executed directly
if __name__ == "__main__":
    Lemayian = WorkingClass("Regular", "Worker", 22, "Kajiado", 22000, "+254700613380")
    Worker = WorkingClass.fromString("James - Lemayian - 50 - Narok - 1000 - Owns no phone")
    print(Lemayian)
    print(WorkingClass.totalExpenditures)
    print(WorkingClass.citizenStats())
    print(Lemayian + Worker)
    # Looking at how the inheritance flows
    # help(WorkingClass)
