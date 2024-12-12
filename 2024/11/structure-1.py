#!/usr/bin/python
import os
import copy

debugmode = False
if debugmode: print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findthing1(testnum):
    if testnum == "0":
        return ["1"]
    if len(testnum) % 2 == 0: # even
        split = int(len(testnum)/2)
        return[testnum[0:split], str(int(testnum[split:]))] # str(int()) to remove leading zeros
    return [str(int(testnum)*2024)]

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split(" ")
    newdata = inputdata.copy()
    for iter in range(1,25+1):
        olddata = newdata.copy()
        newdata = []
        for item in olddata:
            newdata = newdata + findthing1(item)
        if debugmode: print("Iteration ", iter, " : ", newdata)
    return len(newdata)

print(checkeverything(inputfile_source))