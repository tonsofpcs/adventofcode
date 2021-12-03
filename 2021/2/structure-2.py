#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

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
    ha = [directions[testval[0]][0] * int(testval[1]), directions[testval[0]][1] * int(testval[1])]
    return ha

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    horiz = []
    aim = []

    for line in inputdata:
        ha = findthing2(line)
        #print(ha)
        horiz.append(ha[0])
        aim.append(ha[1])
    
    ht = 0
    vt = 0
    curraim = 0
    for index in range(len(horiz)):
        ht += horiz[index]
        curraim += aim[index]
        vt += horiz[index]*curraim

    result1 = ht
    result2 = vt
    result3 = ht * vt

    print("Horiz %s" % result1)
    print("Depth %s" % result2)
    print("Mult %s" % result3)

checkeverything(inputfile_source)