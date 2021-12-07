#!/usr/bin/python
import os
import re
import statistics


print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    crabs = list(map(int, inputdata[0].split(",")))
    maxcrabs = max(crabs)
    #abstractcrabs = [0]*(maxcrabs+1)
    
    #crabsum = 0

    #for index in range(maxcrabs+1):
    #    abstractcrabs[index] = crabs.count(index)
    #    crabsum += index * abstractcrabs[index]

    print(statistics.median(crabs)) #crabsum*1.0/maxcrabs)
    #averagecrab = int(crabsum/maxcrabs)
    averagecrab = int(statistics.median(crabs))
    crabdistance = 0

    #for index, location in enumerate(abstractcrabs):
    for index in range(maxcrabs+1):
        crabdistance += abs(crabs.count(index)*(averagecrab - index))
    
    
    print("Result %s" % crabdistance)
    #print("Result %s" % result2)
    #print("Result %s" % result3)

checkeverything(inputfile_source)