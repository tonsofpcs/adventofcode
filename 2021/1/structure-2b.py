#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findthing1(testrange):
    seekvalue = []
    testints = [int(item) for item in testrange]
    for index in range(len(testints)):
        if index > 1:
            #print(testints[index-2:index+1], sum(testints[index-2:index+1]))
            seekvalue.append(sum(testints[index-2:index+1]))
    return seekvalue

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    count = 0

    movingaverage = findthing1(inputdata)
    
    for index, line in enumerate(movingaverage):
        if (index >= 1):
            if(int(line) > int(movingaverage[index - 1])):
                count += 1
    result1 = count
    print("Result %s" % result1)

checkeverything(inputfile_source)