# Party Attendees
# Created by James Lemayian
# This program askes the users to enter the names of everyone attending a party
# put those values in a list
# sort the list
# print the sorted list

print("Hello, I want to help you get a list of all your party attendees at one place.\n")

attendList = []
attendValue = "Attendee"

while(attendValue.upper() != "DONE"):
    attendValue = input("Attendee's name (input DONE when done) : ").capitalize()
    if(attendValue.upper() != "DONE"):
        attendList.append(attendValue)

attendList.sort()

for person in attendList:
    print(person)
