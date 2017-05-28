
def duplication(x):
    """
    this is the function that creates the expanded binary string s
    and gets the binary value at position x.
    """
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
    return s[x]


def getInput():
    """ get input logic is enclosed in this function. This is mainly for better error handling. """
    try:
        q = int(input("How many postions do you want to check?: ").strip())
        for a0 in range(q):
            x = int(input("Value at position?: ").strip())
            result = duplication(x)
            print(result)
    except ValueError:
        print("Please input an integer value.")
        getInput()
    finally:
        print("Bye bye!")


if __name__ == '__main__':
    getInput()
