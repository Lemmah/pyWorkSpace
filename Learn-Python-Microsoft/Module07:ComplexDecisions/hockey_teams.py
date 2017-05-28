# Teams wishes.
# Created by James Lemayian
# This program just shows how to use flags to see logical errors done away with

teamName = input("Input the team name: ")
teamSport = input("Input the sport: ")

# flag for hockey sport:
sportIsHockey = False
if teamSport.upper() == "HOCKEY":
    sportIsHockey = True

# flag for correct teams:
correctTeam = False
if teamName.lower() == "leads" or teamName.lower() == "senators" \
or teamName.lower() == "rangers":
    correctTeam = True

# use my flags:
if sportIsHockey and correctTeam:
    print("This is an awesome hockey team.")
elif correctTeam:
    print("This is not a hockey team.")
else:
    print("I don't know this team.")


