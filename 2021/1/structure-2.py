#!/usr/bin/python
import os
import copy

print("importing")

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

    count = 0

    for index in range(len(inputdata)):
        if (index >= 2):
            if(int(inputdata[index])+int(inputdata[index - 1])+int(inputdata[index - 2]) > int(inputdata[index - 1])+int(inputdata[index - 2])+int(inputdata[index - 3])):
                count += 1
    result1 = count
    print("Result %s" % result1)

checkeverything(inputfile_source)