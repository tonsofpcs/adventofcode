#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findthing1(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

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
    sortdata =[]
    for line in inputdata:
        sortdata.append(int(line))
    
    sortdata.sort()
    diff = [0,0,0,0]
    for index, line in enumerate(sortdata):
        #print(index)
        #print(int(line) - int(sortdata[index-1]))
        if index == 0:
            diff[int(line) - 0] += 1
        if index > 0:
            diff[int(line) - int(sortdata[index-1])] += 1
    
    return diff[1]*diff[3]

print(checkeverything(inputfile_source))