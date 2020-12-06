#!/usr/bin/python

print "importing"

inputfile_source = "2020/5/input.txt"

def findrow(rowchars):
    row = 128
    testrange = 128
    for c in rowchars:
        testrange = testrange/2
        if (c == "F"):
            row = row - testrange
    row = row - 1
    return row

def findcol(colchars):
    col = 8
    testrange = 8
    for c in colchars:
        testrange = testrange/2
        if (c == "L"):
            col = col - testrange
    col = col - 1
    return col

def findid(passchars):
    return (findrow(passchars[0:7]) * 8 + findcol(passchars[7:10]))

def checkpasses(filename):
    maxid = 0
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for line in inputdata:
        seatid = findid(line)
        if (seatid > maxid):
            maxid = seatid
    return maxid

print(checkpasses(inputfile_source))