#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findthing1(testrange, debugmode = False):
    testvalue = -1
    testdirection = 0
    badlevels = 0
    for itemstr in testrange:
        item = int(itemstr)
        if not(testvalue == -1):
            if(testdirection == 0):
                if (item - testvalue) > 0:
                    testdirection = 1
                elif (item - testvalue) < 0:
                    testdirection = -1
                else:
                    if debugmode: print("Unsafe due to nochange:  ", testrange, testvalue, item, (item - testvalue), testdirection)
                    return 0
            else:
                if not ((item - testvalue) > 0 and testdirection == 1) and not ((item - testvalue) < 0 and testdirection == -1):
                    if debugmode: print("Unsafe due to direction: ", testrange, testvalue, item, (item - testvalue), testdirection)
                    return 0
            if abs(item - testvalue) > 3:
                if debugmode: print("Unsafe due to >3:        ", testrange, testvalue, item, (item - testvalue), testdirection)
                return 0
        testvalue = item
    return 1

def findthing2(testrange):
    for indexvalue in range(len(testrange)):
        testrangecopy = testrange.copy()
        del testrangecopy[indexvalue]
        result = findthing1(testrangecopy, True)
        if result == 1:
            print("Safe", testrange, testrangecopy)
            return 1
    return 0

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    result1 = 0
    for line in inputdata:
        result = findthing1(line.split(" "))
        if result == 1:
            result1 += 1
        else: 
            #try all the options
            result1 += findthing2(line.split(" "))
    print("Result %s" % result1)
    # print("Result %s" % result2)
    # print("Result %s" % result3)

checkeverything(inputfile_source)