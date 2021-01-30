import os
import sys

def answer(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        initialList = [line.split(" ") for line in f.readlines()]
    #print(initialList)

    print(initialList[0][1][0])
    #first index is overall/big list item (list of contents of a single line from input file)
    #second index is which part of the line you want (0 = number of times letter can appear, 1 = letter, 2 = password)
    #third index is which character of resulting string from above 2 indeces you want

    #counter to keep track of valid password count
    validCount = 0

    #i = list of contents of single line from input file)
    for i in initialList:
        #split the first item of each list by hyphen to get min and max count of letters permitted for password
        countList = i[0].split("-")
        minCount = int(countList[0])
        maxCount = int(countList[1])
        letter = i[1][0]
        charCounter = 0
        for ch in i[2]:
            if ch == letter:
                charCounter+=1
        if charCounter >= minCount and charCounter <= maxCount:
            validCount+=1

    print(validCount)

answer("input2.txt")



