# while loops are used when we do not know the end point.
# when we do not have the finite number of times the loops needs to run before it terminates.
# beats the other loops when you do not have an idea upfront.

answer = "0"
while answer != "4":
    answer = input("What is 2 + 2? ")
    if answer != "0":
        if answer != "4":
            print("Ooops, 2 + 2 is not {}".format(answer))
print("Congratulations!! You got it right, 2 + 2 = 4")
