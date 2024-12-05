#!/usr/bin/python
import os
import copy
import numpy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def makegrid(testrange):
    outputgrid = []
    for item in testrange:
        outputgrid.append(list(item))
    return outputgrid

def rotategrid(testrange):
    # print("testing: ", testrange)
    outputgrid = []
    maxrows = len(testrange)
    for rownum, item in enumerate(testrange):
        spaces = [" "]*(rownum)
        spaces2 = [" "]*(maxrows - rownum - 1)
        outputgrid.append(spaces + item + spaces2)
    return numpy.rot90(outputgrid)


def findword(testrange, findstr, directions):
    seekvalue = 0
    for item in testrange:
        seekvalue += ''.join(item).count(findstr)
        seekvalue += ''.join(item).count(findstr[::-1]) if directions else 0
    # print("Count: ", seekvalue)
    return seekvalue

def findgroup(testgroup, findstr):
    seekvalue = 0
    seekvalue += findword(testgroup, findstr, True)
    testgroup90 = numpy.rot90(testgroup)
    seekvalue += findword(testgroup90, findstr, True)
    testgroup45 = rotategrid(testgroup)
    seekvalue += findword(testgroup45, findstr, True)
    testgroup135 = rotategrid(testgroup90.tolist())
    seekvalue += findword(testgroup135, findstr, True)
    return seekvalue
    

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputrows = inputfiledata.split("\n")
    
    grid = makegrid(inputrows)
    
    foundwords = findgroup(grid, "XMAS")
    # print("Result %s" % grid)
    
    print("Result %s" % foundwords)

checkeverything(inputfile_source)