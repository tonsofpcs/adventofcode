#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def checkseat(row, seatindex, thisseat):
    #row.trim("\n","")
    adjacent = 0
    maxseat = len(row)-1
    if not (seatindex == 0):
        adjacent += (row[seatindex-1] == "#")
    if not (thisseat):
        adjacent += (row[seatindex] == "#")
    if not (seatindex == maxseat):
        adjacent += (row[seatindex+1] == "#")
    return adjacent

def runaround(inputdata):
    maxrow = len(inputdata) - 1
    newseats = []
    for rowindex, row in enumerate(inputdata):
        newseats.append( "")
        for seatindex, seat in enumerate(row):
            #print (rowindex, seatindex)
            adjacent = 0
            if seat == ".": #nothing to do for '.'
                newseats[rowindex] += "."
            else:
                if not (rowindex == 0):
                    adjacent += checkseat(inputdata[rowindex-1],seatindex, 0)
                adjacent += checkseat(inputdata[rowindex],seatindex, 1)
                if not (rowindex == maxrow):
                    adjacent += checkseat(inputdata[rowindex+1],seatindex, 0)
                if seat == "L":
                    if adjacent == 0:
                        newseats[rowindex] += "#"
                    else:
                        newseats[rowindex] += "L"
                if seat == "#":
                    if adjacent >= 4:
                        newseats[rowindex] += "L"
                    else:
                        newseats[rowindex] += "#"
    return(newseats)

def countoccupied(inputdata):
    count = 0
    for row in inputdata:
        count += row.count("#")
    return count

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    #maxseat = len(inputdata[0]) - 1
    samesies = 0
    counter = 0
    #print(counter, inputdata)
    while not samesies:
        counter += 1
        newdata = copy.copy(runaround(inputdata))
        #print(counter, newdata)
        #counter += 1
        #newdata = runaround(newdata)
        #print(counter, newdata)
        samesies = (newdata == inputdata)
        inputdata = copy.copy(newdata)
    
    return countoccupied(newdata)


  

print(checkeverything(inputfile_source))