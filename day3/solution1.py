import os
import sys


def answer(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        geography = [[line.strip()] for line in f.readlines()]


    treeCount = 0
    runIncr = int(input("What is the run: "))
    fallIncr = int(input("What is the fall: "))
    run = 0
    fall = 0
    while True:
        run+=runIncr
        fall+=fallIncr

        if fall > 322:
            break
        if run > 30:
            run = run - 31
        #print("row: " + str(fall))
        #print("column: " + str(run))
        print(geography[fall])
        status = geography[fall][0][run]
        #print(status)
        if status == "#":
            treeCount+=1

    print(treeCount)

answer("input.txt")
