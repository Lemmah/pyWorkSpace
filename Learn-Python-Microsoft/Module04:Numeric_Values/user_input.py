# Handling User input
# Created by James Lemayian

salary = input('Please enter your salary: ')
bonus = input('Please enter your bonus: ')
# input function returns a string.
# converting the inputs to int
salary = int(salary)
bonus = int(bonus)
pay_check_amount = salary + bonus

print(pay_check_amount)
