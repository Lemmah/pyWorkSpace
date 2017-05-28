# Reading and writing files with functions
# Done by James Lemayian

from csv import reader
from sys import exc_info


def main():
    """ This main function is the control flow of my program """
    try:
        # user instructions
        welcomeMessage = "Guest Tracker, more effective than a visitor book.\n"
        usageInstruction = "Please input guest details in 'Name,age' format.\n\
        Or input PRINT to print the list of guests in the guest file.\n\
        Or input DONE to exit the program when done!"
        print(welcomeMessage)
        print(usageInstruction)
        # open guestFile, important in handling the FileNotFoundError
        useGuestFile("open")
        # open guestFile and get list of invited guests
        getInvitedGuests()
        # invitedGuests.remove("James Lemayian,20")
        # prompting user to input new guest details and validating guest
        newGuests = getNewGuest()
        # add all the new guests to the guest list
        addNewGuest(newGuests)
        # sort guests after adding them
        sortGuestList()

    except FileNotFoundError:
        print("There was a problem while trying to create the guestFile.csv file.")
    except PermissionError:
        print("Problem occured while writing guestFile.csv: Permission Denied.")
    except:
        print("Something unexpected just happened.")
        error = exc_info()
        print(error)

    finally:
        try:
            # close guestFile
            useGuestFile("close")
        except 1 == 1:
            print("Error: the guestFile.csv file was not found.")


def useGuestFile(operation, mode="READ"):
    """ This is mainly for file operations to the guest file """
    # Flaging my CONSTs
    GUESTFILE = "guestFile.csv"
    READ = "r"
    WRITE = "w"
    APPEND = "a"

    # openning and closing
    try:
        # open the file
        if operation == "open":
            # get the list of guests by default
            if mode == "READ":
                guestFile = open(GUESTFILE, READ)
                return guestFile
            # add the list of new guests
            elif mode == "APPEND":
                guestFile = open(GUESTFILE, APPEND)
                return guestFile
            elif mode == "WRITE":
                guestFile = open(GUESTFILE, WRITE)
                return guestFile

        # close the file
        elif operation == "close":
            guestFile = open(GUESTFILE, READ)
            guestFile.close()
            print("The guestFile.csv file has been successfully closed.")

    except FileNotFoundError:
        # write will create the guestFile.csv
        guestFile = open(GUESTFILE, WRITE)
        print("The guestFile.csv File was missing but a new one has been successfully created.")
        useGuestFile(operation)  # recursively recall this function now with the guest file present


def getInvitedGuests():
    """ Returning a list of invited guests """
    invitedGuestList = []
    guestFile = useGuestFile("open")
    invitedGuests = reader(guestFile)
    for eachGuest in invitedGuests:
        guestDetails = ",".join(eachGuest)
        invitedGuestList.append(guestDetails)
    return invitedGuestList


def getNewGuest():
    """
    Prompt user for input and get all the new guests pass them to the addGuest func
    Exceptions: "DONE" -> exits the program. "PRINT" -> prints the guests who are in guestFile
    """
    newGuests = []
    prompt = ">>> "
    guestDetails = input(prompt)
    guestIsValid = validateGuest(guestDetails)
    # continuously prompt and validate guests
    while guestDetails.upper() != "DONE":
        if guestDetails.upper() == "PRINT":
            print("\nThese are the initial guests. To reflect recent additions, please input DONE and restart the program.\n")
            printGuestList()
            guestDetails = input(prompt)
            guestIsValid = validateGuest(guestDetails)
        elif not guestIsValid or guestDetails in newGuests:
            if len(guestDetails) > 1:
                print("{} is already in the list.".format(guestDetails))
                guestDetails = input(prompt)
                guestIsValid = validateGuest(guestDetails)
            else:
                guestDetails = input(prompt)
                guestIsValid = validateGuest(guestDetails)

        else:
            if len(guestDetails) > 1:
                newGuests.append(guestDetails)
                print("{} has been successfully added.".format(guestDetails))
                guestDetails = input(prompt)
                guestIsValid = validateGuest(guestDetails)
            else:
                guestDetails = input(prompt)
                guestIsValid = validateGuest(guestDetails)
    return newGuests


def validateGuest(guestDetails):
    """
    Validate any guest who is not on the guest list apart from the word "DONE"
    which is used to exit the program.
    """
    validGuest = False
    guestList = getInvitedGuests()
    if guestDetails not in guestList:
        if guestDetails.upper() != "DONE":
            validGuest = True
    return validGuest


def addNewGuest(newGuests):
    """ Adding the newGuests from the newGuestList into the file """
    guestFile = useGuestFile("open", "APPEND")
    for eachGuest in newGuests:
        guestFile.write(eachGuest + "\n")
        print("{} confirmed now in the list.".format(eachGuest))
    status = "New guests have been successfully added."
    return status


def sortGuestList():
    """ Sorting the guestList and rewriting it into the file """
    guestList = getInvitedGuests()
    guestList.sort()
    guestFile = useGuestFile("open", "WRITE")
    for eachGuest in guestList:
        guestFile.write(eachGuest + "\n")
    status = "Guest File has been successfully sorted and written."
    return status


def printGuestList():
    """ Printing the guests who are in the guestFile file """
    invitedGuests = getInvitedGuests()
    for eachGuest in invitedGuests:
        print(eachGuest)
    print("\n")
    status = "Printing guests was successfull."
    return status


if __name__ == "__main__":
    main()
