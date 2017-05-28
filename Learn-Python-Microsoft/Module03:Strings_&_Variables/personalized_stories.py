# Personal Story
# Created by James Lemayian
# This program simply creates a short story about a person based on the details they input.

print('\nPersonalized Story.\n')

user_fname = input('Enter your First Name: ')
user_fname = user_fname.capitalize()
user_lname = input('Enter yor Last Name: ')
user_lname = user_lname.capitalize()
person_name = user_fname + ' ' + user_lname
country = input('Enter your country\'s code: ')
country = country.upper()
hobby = input('What do you like doing when free?: ')
hobby = hobby.lower()

print('Hello, {}.\nIt\'s really nice to meet you!\nYou\'re a very interesting\
 person.\nYou come from {} and your hobby is {}.'.format(person_name, country, hobby))
