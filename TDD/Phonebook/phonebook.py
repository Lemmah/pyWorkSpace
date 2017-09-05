

class Phonebook:
    """ A Phonebook Object """

    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        """ Method to Add Contacts Details """
        self.contacts[name] = number
        return "{} has been added to your list of contacts".format(name)

    def lookup(self, name):
        """ Method to Lookup Contact Details """
        try:
            return self.contacts[name]
        except Exception as e:
            return str(e)

    def delete(self, name):
        """ Method to Delete Contact by Name """
        try:
            del self.contacts[name]
            return "{} has been deleted from your contacts".format(name)
        except Exception as e:
            return str(e)
