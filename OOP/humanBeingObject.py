# Modelling a typical human being

class HumanBeing():
    # Class constructor. Human being has:
    def __init__(self, name="Person", gender="human", age=20, color="black", height=5.6, MPESAPin=1234, MPESABal=22000):
        ''' Class attributes '''
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color
        self.height = height
        self.__pin = MPESAPin
        self.__bal = MPESABal

    # Class Methods
    def speak(self):
        return "I'm {}. Aged {}. Skin color {}. {}".format(self.name, self.age, self.color, self.gender)

    def grow(self):
        self.age += 1

    # Getters and setters
    def getBalance(self):
        enteredPin = int(input("Enter pin: "))
        if enteredPin == self.__pin:
            print("Balance is: ", self.__bal)
        else:
            print("Gerrarahia.")


class Man(HumanBeing):
    def __init__(self, name="Person", age=20, color="black", height=5.6, MPESAPin=1234, MPESABal=22000, beard=True):
        super().__init__(name=name, gender="Male", age=age, height=height, MPESAPin=MPESAPin, MPESABal=MPESABal)
        self.beard = beard

    def maturity(self):
        if beard:
            print("Matured Male")
        else:
            print("Normal Male")


Janet = HumanBeing()
Janet.name = "Janet W"
Janet.gender = "female"
Janet.color = "light-skin"
print(Janet.name)
print(Janet.speak())
Janet.grow()
print(Janet.speak())
# This is encapsulated
#print(Janet.__pin)
Janet.getBalance()
Nderitu = Man("Nderitu", 20, "black", 5.2)
print(Nderitu.speak())
Nderitu.grow()
Nderitu.grow()
print(Nderitu.speak())
