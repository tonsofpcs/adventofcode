#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def maskreplace(base, mask):
    binary = format(base,"036b")
    newbin = ""
    for index, item in enumerate(mask):
        if item == "X":
            newbin += binary[index]
        elif item == "1":
            newbin += "1"
        elif item == "0":
            newbin += "0"
        else:
            print("ERROR.  Bad Mask.", mask)
    return int(newbin,2)


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
            address = int(linedata[0].replace("]","")[4:])
            if address in indexbase:
                pass #TODO: Replace data
                location = indexbase.index(address)
                database[location] = maskreplace(int(linedata[1]),maskdata)
                #print(address, database[location])
            else:
                indexbase.append(address)
                database.append(maskreplace(int(linedata[1]),maskdata))
                #print(address, database[location])
        else:
            print("ERROR.  Invalid command, ", linedata[0])
            return("ERROR")
    return sum(database)

print(checkeverything(inputfile_source))