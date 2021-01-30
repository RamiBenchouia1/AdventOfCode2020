import os
import sys

def answer(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        expenseReport = [int(line.strip()) for line in f.readlines()]

    #nested for loop to add every possible combination of two numbers in the list, find its complement (to sum to 2020) and see if that complement exists in the list, if so then multiply all numbers and break out of loop
    for i in range(0,len(expenseReport)-1):
        baseValue = expenseReport[i]
        for j in range(1,len(expenseReport)):
            secondValue = expenseReport[j]
            sumVal = baseValue+secondValue
            complement = 2020 - sumVal
            if complement in expenseReport:
                answerValue = baseValue*secondValue*complement
                break

    print(answerValue)

answer("input.txt")