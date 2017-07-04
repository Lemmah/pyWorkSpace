# creating a calculator module to illustrate use of classes

class Calculator:
    ''' A simple calculator module '''

    def add(num1, num2):
        ''' sum of two numbers '''
        addition = num1 + num2
        return addition

    def sub(num1, num2):
        ''' subtrating the second num from the first '''
        subtraction = num1  - num2
        return subtraction

    def mult(num1, num2):
        ''' multiplication between two numbers '''
        multiplication = num1 * num2
        return multiplication

    def divide(num1, num2):
        ''' dividing the fist number by the second.'''
        division = num1/num2
        return division

def calculate():
    ''' sort of the main function to drive the calculator '''
    print("Welcome to our beautiful calculator.")
    num1, num2 = [int(number.strip()) for number in input("Please enter two numbers. num1, num2: ").split(",")]
    operation = input("What do you want to do?\n\
    1. Add\n\
    2. Subtract\n\
    3. Multiply\n\
    4. Divide\n")
    if int(operation) == 1:
        result = Calculator.add(num1,num2)
        print("Result of {} added to {} is {}".format(num1, num2, result))
    elif int(operation) == 2:
        result = Calculator.sub(num1, num2)
        print("Result of {} subtracted from {} is {}".format(num2, num1, result))
    elif int(operation) == 3:
        result = Calculator.mult(num1, num2)
        print("Result of {} multiplied with {} is {}".format(num1, num2, result))
    elif int(operation) == 4:
        result = Calculator.divide(num1, num2)
        print("Result of {} divided by {} is {}".format(num1, num2, result))

# For modularization
if __name__ == "__main__":
    calculate()
