#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

directions = {
    'forward': [1,0],
    'backward': [-1,0],
    'up': [0,-1],
    'down': [0,1]
}

def findthing1(testrange):
    seekvalue = []
    seekvalue = testrange.split(" ")
    return seekvalue

def findthing2(testrange):
    testval = findthing1(testrange)
    hv = [directions[testval[0]][0] * int(testval[1]), directions[testval[0]][1] * int(testval[1])]
    return hv

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    horiz = []
    vert = []

    for line in inputdata:
        hv = findthing2(line)
        print(hv)
        horiz.append(hv[0])
        vert.append(hv[1])
    
    result1 = sum(horiz)
    result2 = sum(vert)
    result3 = result1 * result2

    print("Horiz %s" % result1)
    print("Depth %s" % result2)
    print("Mult %s" % result3)

checkeverything(inputfile_source)