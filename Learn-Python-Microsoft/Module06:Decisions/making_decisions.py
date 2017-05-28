# Making Decisions
# Created by James Lemayian

# if statements with strings
best_team = 'senators'
favorite_team = input('What is your favorite hockey team? ')
if favorite_team.capitalize() == best_team.capitalize() :
    print('Yeah Go Sens Go!')
    print('But I miss Alfresson.')
print('It\'s okay if you prefer soccer to hockey.')

# if statements with numbers
deposit = input('How much do you want to deposit? ')
# setting a flag: reducing chances of making a mistake
free_toaster = False
if int(deposit) > 100:
    free_toaster = True

# using my flag.
if free_toaster :
    print('Enjoy your free toaster!')
else:
    print('Enjoy your free mug!')

print('Have a nice day!')

