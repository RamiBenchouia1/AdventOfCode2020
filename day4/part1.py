import os
import sys


def listOfEntries(someList):
    entryList = []
    entryString = ""
    for item in someList:
        subList = []
        if item != "": #append each string to temp/holder variable "entryString" which accumulates contents of each entry 
            entryString += item + " "
        else: #if empty string is encountered, this implies that we have finished with one entry and new list needs to be created
            modString = entryString[:-1] #removes space character that is inadvertantly added when last item is appended
            subList.append(modString) #create a list of a single string that contains text from all lines of txt file corresponding to 1 entry
            entryList.append(subList) #list of lists, where each sublist contains 1 string with all lines from original txt file corresponding to 1 entry
            entryString = "" #reset the variable entry string for next entry

    return entryList

def answer(inputFile):
    with open(os.path.join(sys.path[0], inputFile), "r") as f:
        passports = [line.strip() for line in f.readlines()]
        #creates list of strings, each element of list is string of each whole line, includes empty lines

    entryList = listOfEntries(passports)
    print(entryList)

    validTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validPassports = 0
    for unit in entryList:
        if all(x in unit[0] for x in validTerms): #returns boolean that indicates if items in validTerms are all contained in string representing single entry (thus indicating if it is a valid passport entry or not)
            validPassports += 1 #if true = if valid possport (then increase counter)

    print(validPassports)


answer("input.txt")