# Open my File

# animalFile = open("Tasmania.txt", "r")
# better way of opening file
with open("Tasmania.txt", "r") as animalFile:

    # read all file contents
    # allFileContents = animalFile.read()
    # print(allFileContents)

    # read line by line
    firstAnimal = animalFile.readline()
    print(firstAnimal)
    secondAnimal = animalFile.readline()
    print(secondAnimal)
