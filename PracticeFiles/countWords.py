# Write a program that prompts the user foa sentence and then counts the number of same words in the sentence.

def words():
    sentence = input("Please enter a sentence: ").strip()
    sentList = sentence.split(" ")
    print(sentList)

    wordCount = {}

    for eachWord in sentList:
        if eachWord in wordCount.keys():
            wordCount[eachWord] += 1
        else:
            wordCount[eachWord] = 1

    print(wordCount)


words()
