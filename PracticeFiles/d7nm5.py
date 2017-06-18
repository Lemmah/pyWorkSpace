
def calcNum():
    '''
    A function which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained are printed in a comma-separated sequence on a single line.
    '''
    # list of valid numbers which satisfy the conditions
    validNum = []
    # range of 2000 and 3200 both included
    for num in range(1999, 3201):
        divisibleBy7 = (num % 7 == 0)
        multipleOf5 = (num % 5 == 0)
        if divisibleBy7 and not multipleOf5:
            validNum.append(num)
        else:
            continue

    return validNum


print(", ".join(map(str,calcNum())))
