# Loan Calculator
# Created by James Lemayian
# Microsoft Virtual Academy Assignment

loan_amount = input('Please enter the cost of the loan: ')
interest_rate = input('Please enter the interest rate in %: ')
repay_years = input('Please enter the number of years: ')
# creating variables that work with the formular
# M = monthly payment
L = int(loan_amount)
i = int(interest_rate)/100
n = int(repay_years) * 12

M = (L * i * (1 + i) * n)/((1 + i) * (n-1))

print('You will repay your loan in monthly installments of {0:.2f} \
for {1:02d} months'.format(M, n))
