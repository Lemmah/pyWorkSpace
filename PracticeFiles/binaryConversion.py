name = "lemayian"
binaryLetters = []
for letter in name:
    binary_number = format(ord(letter), 'b')
    binaryLetters.append(binary_number)
    print(binary_number)

print("\nBinary Letters")
print(binaryLetters)

joinedList = "".join(binaryLetters)
print("\nJoined List:")
print(joinedList)

