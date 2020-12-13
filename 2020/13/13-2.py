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
    starttime = int(inputdata[0])
    busdata = inputdata[1].split(",")
    busses = []
    for item in busdata:
        if not (item == "x"):
            busses.append(int(item))
            
    nextstart = []
    for bus in busses:
        nextstart.append(bus - starttime % bus)
        #print(starttime, bus, bus - (starttime % bus))
    busindex = nextstart.index(min(nextstart))
    return busses[busindex] * nextstart[busindex]

print(checkeverything(inputfile_source))