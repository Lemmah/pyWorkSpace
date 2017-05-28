# Manipulating Numbers
# Created by James Lemayian

area = 0
height = 10
width = 20

# calculate the area of a triangle
area = width * height/2

print(area)

# formatting the area to a float with 2 decimal places
print('The area of the triangle would be %.2f.' % area)

# formatting a number to hold 4 spaces.
print('This %3d holds 4 spaces' % 23)
# formating with 0 for extra spaces.
print('This %03d has 4 spaces with leading zeros.' % 23)

# using the format method to format numeric values.
# normal decimal
print('I have {0:d} cats.'.format(6))
# decimal with leading spaces
print('I have {0:3d} cats.'.format(6))
# decimal with leading spaces as zeros
print('I have {0:03d} cats.'.format(6))
# floats
print('I have {0:f} cats.'.format(6))
# floats with specified number of decimal places.
print('I have {0:.2f} cats.'.format(6))

# format method?
print('This is {0} new way of formatting python {1} text. It \
is {2}!'.format('the','args','awesome'))
