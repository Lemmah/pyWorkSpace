# Modelling a normal human being


class Human():
    ''' This class is just of a normal human being object. '''
    def __init__(self, humanGender="unknown", age=0, mungerLevel="peaceful", hungerLevel=0):
        self.humanGender = humanGender
        self.age = age
        self.mungerLevel = mungerLevel
        self.hungerLevel = hungerLevel

    def setGender(self):
        self.humanGender = input("Please enter the human's gender: ")

    def setAge(self):
        self.age = int(input("Please enter human age: "))

    def setHungerLevel(self):
        self.hungerLevel = int(input("Please enter the hunger level: "))

    def setMungerLevel(self):
        if self.hungerLevel <= 2:
            self.mungerLevel = "The human is still very peaceful."
        elif self.hungerLevel <= 5:
            self.mungerLevel = "The human is getting narky!"
        elif self.hungerLevel <= 8:
            self.mungerLevel = "The human is getting aggressive but still in control."
        else:
            self.mungerLevel = "The human is very aggressive. Quite dangerous."
        return (self.mungerLevel)


Lemayian = Human()
Lemayian.setAge()
Lemayian.setHungerLevel()
Lemayian.setMungerLevel()

print("Lemayian is {} years old. {}".format(Lemayian.age, Lemayian.mungerLevel))
