# Reading and Writing invited guests.
# Done by James Lemayian

import csv

# Flaging my CONSTs: this is convection.
INVITEDGUESTS = "invitedGuests.csv"
READ = "r"
WRITE = "w"
APPEND = "a"

print("\nWe're helping you keep track of your guests. Please enter their names and ages in 'Names, age' format.")

guestList = []
# get the file guest list and append it to guestList variable
with open(INVITEDGUESTS, READ) as getGuests:
    oldGuestList = csv.reader(getGuests)
    for eachGuest in oldGuestList:
        guestDetails = ", ".join(eachGuest)
        if guestDetails != "Names, age":
            guestList.append(guestDetails)

# clear the list from file.
with open(INVITEDGUESTS, WRITE) as clearGuests:
    clearGuests.write("Names, age\n")


guestDetails = "attendeeName, Age"
invalidGuest = False

while not invalidGuest:
    guestDetails = input("Enter Name, age (enter DONE if you're done) : ")
    guestDetails = guestDetails.capitalize()
    if guestDetails.upper() == "DONE":
        invalidGuest = True
    if not invalidGuest:
        if guestDetails not in guestList:
            guestList.append(guestDetails)
            print("{} has been successfully added.".format(guestDetails))
        else:
            print("{} is already in the list.".format(guestDetails))
        guestList.sort()

for guest in guestList:
    with open(INVITEDGUESTS, APPEND) as addGuests:
        addGuests.write(guest + "\n")
        print("{} has been confirmed".format(guest))

print("\n\tBye! Bye!\n\n")
# print(",".join(guestList))
