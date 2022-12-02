#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findthing1(testrange):
    currentvalue = 0
    calorielist = []
    for item in testrange:
        print(item)
        if (item == ""):
            calorielist.append(currentvalue)
            currentvalue = 0
        else:
            currentvalue += int(item)
    calorielist.append(currentvalue)
    return calorielist

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
    elves = findthing1(inputdata)
    #for line in inputdata:
        #result2 = findthing2(line)
        #result3 = findgroup(line)
    highelves = 0
    print("Result %s" % elves)
    elfmax = max(elves)
    highelves += elfmax
    print("Result %s" % elfmax)
    elves.remove(elfmax)
    elfmax = max(elves)
    highelves += elfmax
    print("Result %s" % elfmax)
    elves.remove(elfmax)
    elfmax = max(elves)
    highelves += elfmax
    print("Result %s" % elfmax)
    print("Result %s" % highelves)

checkeverything(inputfile_source)