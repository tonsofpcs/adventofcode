#!/usr/bin/python
import os
import copy
import numpy

print("importing")
debugmode = 1

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

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
    # return(outputgrid)

# def rotategridb(testrange):
#     # print("testing: ", testrange)
#     outputgrid = []
#     maxrows = len(testrange)
#     for rownum, item in enumerate(testrange):
#         spaces2 = [" "]*(rownum)
#         spaces = [" "]*(maxrows - rownum - 1)
#         outputgrid.append(spaces + item + spaces2)
#     # return numpy.rot90(outputgrid)
#     return(outputgrid)


def findcross(testrange, findstr, directions):
    seekvalue = 0
    maxrows = len(testrange)
    for rownum, item in enumerate(testrange):
        if debugmode: print(rownum, testrange[rownum])
        if(rownum > 1 and rownum < maxrows - 2):
            offset = 0
            location = 0
            while location > -1:
                location = ''.join(item[offset:]).find(findstr)
                # print(item[offset:])
                # print("location:", location)
                if location > -1:
                    # print("location:", location)
                    rawlocation = location + offset
                    if debugmode: print(rawlocation)
                    if debugmode: print(testrange[rownum-2][rawlocation:][:3])
                    if debugmode: print(testrange[rownum][rawlocation:][:3])
                    if debugmode: print(testrange[rownum+2][rawlocation:][:3])
                    if (testrange[rownum-2][rawlocation] == findstr[0] and testrange[rownum+2][rawlocation+2] == findstr[2]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation+2] == findstr[0] and testrange[rownum+2][rawlocation] == findstr[2]):
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation+2] == findstr[2] and testrange[rownum+2][rawlocation] == findstr[0]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation] == findstr[2] and testrange[rownum+2][rawlocation+2] == findstr[0]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    offset += location + 1
                else:
                    break
    if not directions == True:
        print("one way")
        return seekvalue
    for rownum, item in enumerate(testrange):
        print(rownum, testrange[rownum])
        if(rownum > 0 and rownum < maxrows):
            offset = 0
            location = 0
            while location > -1:
                location = ''.join(item[offset:]).find(findstr[::-1])
                # print(item[offset:])
                if location > -1:
                    # print("location:", location)
                    rawlocation = location + offset
                    if debugmode: print(rawlocation)
                    if debugmode: print(testrange[rownum-2][rawlocation:][:3])
                    if debugmode: print(testrange[rownum][rawlocation:][:3])
                    if debugmode: print(testrange[rownum+2][rawlocation:][:3])
                    if (testrange[rownum-2][rawlocation] == findstr[0] and testrange[rownum+2][rawlocation+2] == findstr[2]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation+2] == findstr[0] and testrange[rownum+2][rawlocation] == findstr[2]):
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation+2] == findstr[2] and testrange[rownum+2][rawlocation] == findstr[0]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    if (testrange[rownum-2][rawlocation] == findstr[2] and testrange[rownum+2][rawlocation+2] == findstr[0]):
                        # cross found
                        if debugmode: print("found")
                        seekvalue += 1
                    offset += location + 1
                else:
                    break
    print("Count: ", seekvalue)
    return seekvalue

def findgroup(testgroup, findstr):
    seekvalue = 0
    # # seekvalue += findcross(testgroup, findstr, True)
    # testgroup90 = numpy.rot90(testgroup)
    # # seekvalue += findcross(testgroup90, findstr, True)
    testgroup45 = rotategrid(testgroup)
    seekvalue += findcross(testgroup45, findstr, True)
    # testgroup135 = rotategrid(testgroup90.tolist())
    # seekvalue += findcross(testgroup135, findstr, True)
    return seekvalue
    

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputrows = inputfiledata.split("\n")
    
    grid = makegrid(inputrows)
    
    foundwords = findgroup(grid, "MAS")
    # print("Result %s" % grid)
    
    print("Result %s" % foundwords)

checkeverything(inputfile_source)