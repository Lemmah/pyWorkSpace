s = "0"
t = ""
while len(s) < 1000:
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
    print("{}\t{}\t{}\n".format(initialS, t, s))
