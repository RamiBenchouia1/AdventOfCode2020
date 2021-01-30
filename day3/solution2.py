import os
import sys


def answer(inputFile, runIncrement, fallIncrement):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        geography = [[line.strip()] for line in f.readlines()]


    treeCount = 0
    # runIncr = int(input("What is the run: "))
    # fallIncr = int(input("What is the fall: "))
    run = 0
    fall = 0
    while True:
        run+=runIncrement
        fall+=fallIncrement

        if fall > 322:
            break
        if run > 30:
            run = run - 31
        #print("row: " + str(fall))
        #print("column: " + str(run))
        #print(geography[fall])
        status = geography[fall][0][run]
        #print(status)
        if status == "#":
            treeCount+=1

    return treeCount
   #print(treeCount)

#answer("input.txt", 3, 1)

tot = 1
for group in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    runIncr = group[0]
    fallIncr = group[1]
    tot = tot * answer("input.txt",runIncr,fallIncr)
    print(tot)
