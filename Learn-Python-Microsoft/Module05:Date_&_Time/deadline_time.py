# Deadlines
# Created by James Lemayian
# This program calculates how many weeks and days one has to the deadline

from datetime import datetime as dt
# imported as dt for faster typing, you know vi has no intellisense

current_date = dt.now().date()
dead_line = input('\nPlease input the deadline of your project (dd/mm/yyyy): \n')
dead_line = dt.strptime(dead_line, '%d/%m/%Y').date()
day_diff = dead_line - current_date
num_of_days = day_diff.days
num_of_weeks = num_of_days//7
rem_days = num_of_days % 7
print('\nYou have {0:d} weeks and {1:d} days remaining.\
'.format(num_of_weeks, rem_days))
