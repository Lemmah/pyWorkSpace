'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
    8
Then, the output should be:
    40320
'''

def numFactorials():
    ''' Get list of numbers from user and return the list of factorials '''
    # get the list of numbers from user
    numbersList = [int(num) for num in input("Input list of numbers separated by a space: ").split()]
    # get the list of factorials by computation
    factorialsList = [calcFactorial(num) for num in numbersList]
    return factorialsList


def calcFactorial(num):
    ''' Recursive function to calculate the factorial. '''
    # base case
    if num <= 1:
        return num
    else:
        return num * calcFactorial(num -1)


print(", ".join(map(str,numFactorials())))
