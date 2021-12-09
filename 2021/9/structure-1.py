#!/usr/bin/python
import os
import copy
import sys

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
    array = []
    for line in inputdata:
        array.append(list(map(int,list(line))))
    
    print(array)
    
    width = len(array[0])
    height = len(array)
    lowrisk = 0
    for y in range(height):
        for x in range(width):
            adjacents = []
            if x-1 > -1:
                adjacents.append(array[y][x-1])
            if y-1 > -1:
                adjacents.append(array[y-1][x])
            if x+1 < width:
                adjacents.append(array[y][x+1])
            if y+1 < height:
                adjacents.append(array[y+1][x])
            adjacents.sort()
            thisone = array[y][x]
            if thisone < adjacents[0]:
                print(x, y, thisone, adjacents)
                lowrisk += thisone + 1


    print("Result %s" % lowrisk)
    # print("Result %s" % result2)
    # print("Result %s" % result3)

checkeverything(inputfile_source)