# The tax lab challenge
import sys


def calculate_tax(individual_income):
    """
   A function to calculate tax of a dictionary pair of names, annualIncome.
   Returns the yearly tax bills in names, annualTax dictionary.
   """

    people = {}
    if isinstance(individual_income, dict):
        for value in individual_income:
            tax = 0
            first_slab = 0
            second_slab = (10000 - 1000) * 0.1
            third_slab = (20200 - 10000) * 0.15
            fourth_slab = (30750 - 20200) * 0.2
            fifth_slab = (50000 - 30750) * 0.25
            if individual_income[value] < 1000:
                tax += first_slab
            elif individual_income[value] > 1000 and individual_income[value] <= 10000:
                tax += first_slab + (individual_income[value] - 1000) * 0.1
            elif individual_income[value] > 10000 and individual_income[value] <= 20200:
                tax += first_slab + second_slab + (individual_income[value] - 10000) * 0.15
            elif individual_income[value] > 20200 and individual_income[value] <= 30750:
                tax += first_slab + second_slab + third_slab + (individual_income[value] - 20200) * 0.2
            elif individual_income[value] > 30750 and individual_income[value] <= 50000:
                tax += first_slab + second_slab + third_slab + fourth_slab + (individual_income[value] - 30750) * 0.25
            else:
                tax += first_slab + second_slab + third_slab + fourth_slab + fifth_slab + (individual_income[value] - 50000) * 0.3
            people[value] = tax
        return people
    else:
        print("The provided input is not a dictionary")

