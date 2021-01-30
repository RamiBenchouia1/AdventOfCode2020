import os
import sys

def answer(fileToRead):
    #open/read the file and append each number to an empty list
    with open(os.path.join(sys.path[0], fileToRead), "r") as f:
        stringArr = [line.strip() for line in f.readlines()]
    
    #iterate through resulting list and instead of doing nested for loop, just use python .index() method to see if 2020 complement exists in list
    for i in stringArr:
        complement = 2020 - int(i) #elements of list are string types, have to cast to int
        itemToFind = str(complement) #convert back to string to see if it exists in list
        if itemToFind in stringArr: 
            answer = int(i)*complement
            print(answer)
            break #break out of loop since you don't have to keep looking anymore

answer("input.txt")