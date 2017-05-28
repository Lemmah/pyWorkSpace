# Manipulating strings
# Created by James Lemayian
# Microsoft Visual Academy

message = input('Input anything: ')
print(message.upper()) # convert to uppercase
print(message.lower()) # convert to lowercase
print(message.swapcase()) # toggle the case
print(message.find('World')) # returns the index of the first letter in the word world if found in the string
print(message.count('o')) # returns the number of occurences of o in the message
print(message.capitalize()) # capitalizes the first letter of the string
print(message.replace('Hello', 'Hi')) # finds hello and replaces it with hi
