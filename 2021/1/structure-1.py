#!/usr/bin/python
import os
import copy

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
    for line in inputdata:
        result1 = findthing1(line)
        result2 = findthing2(line)
        result3 = findgroup(line)
    print("Result %s" % result1)
    print("Result %s" % result2)
    print("Result %s" % result3)

checkeverything(inputfile_source)