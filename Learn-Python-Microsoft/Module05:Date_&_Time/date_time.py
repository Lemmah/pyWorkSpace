# Date-time usage.
# Created by James Lemayian
# Microsoft Visual Academy

import datetime
# the datetime class has the date function in it.

current_date = datetime.date.today() # within the function is a method called today.
print(current_date)
# Within the method we got attributes/properties about the date object.
print(current_date.year)
print('{0:02d}'.format(current_date.month))
print(current_date.day)

# formatting the date and time
print(current_date.strftime('%d-%b-%Y'))
print(current_date.strftime('%d %B, %Y'))

# printing a sentence with the date and time inside
print(current_date.strftime('Please attend our event which is on the %A %d of %B in the year %Y.'))

# accepting date input from users
birth_date = input('Please input your birthday in dd/mm/yyyy format: ')
birth_day = datetime.datetime.strptime(birth_date, '%d/%m/%Y').date()
print(birth_day)

days = current_date.year - birth_day.year
print(days)


# Time formats now!
current_time = datetime.datetime.now()
print(current_time.minute)
print(current_time.hour)
print(current_time.second)
print(current_time.year)
print(current_time.month)
