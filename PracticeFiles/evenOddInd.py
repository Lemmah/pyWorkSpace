stringList = []
testCases = int(input())
# accepting the number of strings specified
while(testCases > 0):
    stringInput = input()
    stringList.append(stringInput)
    testCases -= 1

# printing the characters according to their indices
for eachString in stringList:
    evenIndexed, oddIndexed = [], []
    for character in eachString:
        if eachString.index(character) % 2 == 0:
            evenIndexed.append(character)
        else:
            oddIndexed.append(character)
    print("{} {}".format("".join(evenIndexed), "".join(oddIndexed)))
