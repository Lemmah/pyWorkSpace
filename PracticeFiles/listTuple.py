'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
    34,67,55,33,12,98
    Then, the output should be:
        ['34', '67', '55', '33', '12', '98']
        ('34', '67', '55', '33', '12', '98')
'''

listInput = [str(num) for num in input("Input a list of numbers seperated by comma: ").strip().split(",")]
tupleInput = tuple(listInput)
print(listInput)
print(tupleInput)
