import re
import os
import sys

def openFile(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        #passports = [line.strip().split("\n\n") for line in f.readlines()]

        # for line in f.readlines():
        #     first = line.strip()
        #     some = first.split("\n")
        #     print(some)

        data = f.read()
    
    passports = data.split("\n\n")
    print(passports)

    listSplit = re.split(" |\n", passports)
    print(listSplit)


openFile('input.txt')