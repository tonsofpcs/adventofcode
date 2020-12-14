#!/usr/bin/python
import os
import copy
from datetime import datetime

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

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
    starttime = int(inputdata[0])
    busdata = inputdata[1].split(",")
    busses = []
    intbusdata = []
    for item in busdata:
        if item == "x":
            intbusdata.append(-1)
        else:
            intbusdata.append(int(item))
    sortdata = copy.copy(intbusdata)
    sortdata.sort(reverse = True)
    for item in sortdata:
        if not (item == -1):
            busses.append([int(item),intbusdata.index(item),0])
    maxbus = max(sortdata)
    countindex = maxbus - intbusdata.index(maxbus)
    #print(sortdata)
    #print(busses)
    while countindex < 0:
        countindex += maxbus
    countindex -= maxbus
    notfound = 1
    busses.pop(0) #no need to check the first one
    while notfound:
        countindex += maxbus
        notfound = 0
        for index, [bus, busindex, busfound] in enumerate(busses):
            #print(bus,busindex)
            if (countindex + busindex) % bus:
                notfound = 1 
                break
            else:
                print("Found %s (%s) at %s!" % (bus, busindex, countindex))
                if busfound == 0:
                    busses[index] = [bus, busindex, 1]
    return countindex


print(datetime.now())
print(checkeverything(inputfile_source))
print(datetime.now())