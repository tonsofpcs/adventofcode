#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

openblocks = ['(','[','{','<']
closeblocks = [')',']','}','>']
errorpoints = [3,57,1197,25137]
numblocks = len(openblocks)

def findfirsterror(testrange):
    # countblocks = [0]*numblocks
    blockstack = []
    for value in list(testrange):
        if value in openblocks:
            blockindex = openblocks.index(value)
            blockstack.append(blockindex)
        if value in closeblocks:
            blockindex = closeblocks.index(value)
            # print(blockstack)
            oldindex = blockstack.pop()
            if oldindex != blockindex:
                print(openblocks[oldindex], closeblocks[blockindex])
                return errorpoints[blockindex]
    return 0

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (findfirsterror(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    errorpointtotal = 0
    count = 0
    for line in inputdata:
        count += 1
        print(count)
        errorpointtotal += findfirsterror(line)
        # result2 = findthing2(line)
        # result3 = findgroup(line)
    
    print("Result %s" % errorpointtotal)
    # print("Result %s" % result2)
    # print("Result %s" % result3)

checkeverything(inputfile_source)