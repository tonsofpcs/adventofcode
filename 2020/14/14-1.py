#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findthing1(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def maskreplace(base, mask):
    for item in testrange:
        seekvalue = 1
    return seekvalue

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    maskdata = ""
    indexbase = []
    database = []
    location = 0
    for line in inputdata:
        linedata = line.split(" = ")
        if linedata[0] == "mask":
            maskdata = linedata[1]
        elif linedata[0][0:3] == "mem":
            address = int(linedata[0].replace("]","")[5:])
            if address in indexbase:
                pass #TODO: Replace data
                location = indexbase.index(address)
                database[location] = maskreplace(linedata[1],maskdata)
            else:
                indexbase.append(address)
                database.append(maskreplace(linedata[1],maskdata))
        else:
            print("ERROR.  Invalid command, ", linedata[0])
            return("ERROR")
    
    return database.sum()

print(checkeverything(inputfile_source))