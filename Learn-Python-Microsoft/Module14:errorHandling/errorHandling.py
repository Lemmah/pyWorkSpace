# Error Handling
# Done by James Lemayian

# Simple division calculator
import sys

firstNumber = input("Enter the first number: ")
secondNumber = input("Enter the second number: ")

try:
    firstNumber = float(firstNumber)
    secondNumber = float(secondNumber)

    divident = firstNumber / secondNumber
    print(divident)

except ZeroDivisionError:
    print("The answer is infinity.")

except ValueError:
    print("Please input valid numbers. Be sure not to input letters or '' marks.")

except:
    print("Sorry, something weird just happened. Please contact your system admin.")
    error = sys.exc_info()[0]
    print(error)

finally:
    print("Have a good day!")
