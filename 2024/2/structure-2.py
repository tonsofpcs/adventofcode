#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findthing1(testrange):
    testrange = testrange.split(" ")
    testvalue = -1
    testdirection = 0
    for itemstr in testrange:
        item = int(itemstr)
        if not(testvalue == -1):
            if(testdirection == 0):
                if (item - testvalue) > 0:
                    testdirection = 1
                elif (item - testvalue) < 0:
                    testdirection = -1
                else:
                    print("Unsafe due to nochange:  ", testrange, testvalue, item, (item - testvalue), testdirection)
                    return 0 # unsafe
            else:
                if not ((item - testvalue) > 0 and testdirection == 1) and not ((item - testvalue) < 0 and testdirection == -1):
                    print("Unsafe due to direction: ", testrange, testvalue, item, (item - testvalue), testdirection)
                    return 0 #unsafe
            if abs(item - testvalue) > 3:
                print("Unsafe due to >3:        ", testrange, testvalue, item, (item - testvalue), testdirection)
                return 0 # unsafe
        testvalue = item
    return 1

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    result1 = 0
    for line in inputdata:
        result1 += findthing1(line)
        # result2 = findthing2(line)
        # result3 = findgroup(line)
    print("Result %s" % result1)
    # print("Result %s" % result2)
    # print("Result %s" % result3)

checkeverything(inputfile_source)