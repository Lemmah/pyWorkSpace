# Encapsulation: data hiding. Encapsulated variables cannot be accessed directly.

class BankAccount:
    ''' This is a bank account class '''
    def __init__(self, accountName="Current Account", balance=200):
        ''' Constructor with encapsulated attributes '''
        self.__accountName = accountName
        self.__balance = balance

    def getBalance(self):
        return self.__balance


accountObject = BankAccount()

'''
If you did this, you will encounter errors...
print(accountObject.__accountName)
print(accountObject.__balance)
'''
# Now, how do we get along? Use getters and setters

accountObject = BankAccount()
print(accountObject.getBalance())

