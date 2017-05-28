import sys


def duplication(x):
    # Complete this function
    s = "0"
    t = ""
    while len(s) < 1001:
        tChar = []
        for character in s:
            binaryEq = bin(int("1", 2) - int(character, 2))[2:]
            tChar.append(binaryEq)
        # creating the t
        t = "".join(tChar)
        # capturing initial s
        initialS = s
        # expanding s
        s = initialS + t

    # return value at specified position
    counter = 0
    for eachChar in s:
        if counter == x:
            return eachChar
        else:
            counter += 1


q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x)
    print(result)
