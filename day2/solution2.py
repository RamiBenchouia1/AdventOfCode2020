import os
import sys

def answer(inputFile):

    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        initialList = [line.strip().split(" ") for line in f.readlines()]

    validCounter = 0
    for i in initialList:
        positionList = i[0].split("-")
        firstIndex = int(positionList[0]) - 1
        secondIndex = int(positionList[1]) - 1
        character = i[1][0]
        charCounter = 0
        firstLetter = i[2][firstIndex]
        secondLetter = i[2][secondIndex]

        bool1 = str(firstLetter == character)
        bool2 = str(secondLetter == character)

        if bool1 == "True":
            charCounter+=1

        if bool2 == "True":
            charCounter+=1
        
        if charCounter == 1:
            validCounter+=2

    print(validCounter)

answer("input2.txt")