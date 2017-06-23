# Demonstrating inheritance in python OOP

class Human():
    ''' The normal human object simulation. '''
    def __init__(self, name="Human", age=0, home="Earth", gender="Unknown gender"):
        self.name = name
        self.age = age
        self.home = home
        self.gender = gender

    def introducePerson(self):
        print("Hello, I'm {}. Aged {}. I live in {}.".format(self.name, self.age, self.home))

    def sayGender(self):
        print("{} is {}.".format(self.name, self.gender))


class Man(Human):
    ''' A man, inheriting from the normal human. '''
    def __init__(self, name, age, home, humour="blunt"):
        super().__init__(name=name, age=age, home=home, gender="Male")
        self.humour = humour

    def introducePerson(self):
        if self.humour == "blunt":
            print("Hello, I'm {}. Aged {}. I live in {}.".format(self.name, self.age, self.home))
        else:
            print("Hello, I'm {}. Aged {}. I live in {}. I'm funny and I know that!".format(self.name, self.age, self.home))



Lemayian = Human("James Lemayian",30,"Nairobi")
Lemayian.introducePerson()
Lemayian.sayGender()
Lemayian.gender = "Male"
Lemayian.sayGender()

James = Man("James Lemayian",30,"Nairobi")
James.introducePerson()
James.sayGender()
James.humour = "funny"
James.introducePerson()
