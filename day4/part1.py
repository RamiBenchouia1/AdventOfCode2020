import re
import os
import sys


def answer(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        passports = [line.strip() for line in f.readlines()]

        #print(passports)

    entryList = []
    entryString = ""
    for item in passports:
        subList = []
        if item != "":
            entryString += item + " "
        else:
            modString = entryString[:-1]
            subList.append(modString)
            entryList.append(subList)
            entryString = ""


    validTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validPassports = 0
    for unit in entryList:
        if all(x in unit[0] for x in validTerms):
            validPassports += 1

    print(validPassports)


answer("input.txt")