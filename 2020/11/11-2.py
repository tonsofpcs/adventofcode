#!/usr/bin/python
import os
import copy

seatcount = 5

directiontable = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def checkseat(rowindex, seatindex, seatdata):
    #row.trim("\n","")
    adjacent = 0
    maxseat = len(seatdata[0])-1
    maxrow = len(seatdata) - 1
    minrow = 0
    minseat = 0
    for direction in directiontable:
        foundseat = 0
        x = seatindex
        y = rowindex
        while not(foundseat):
            x += direction[0]
            y += direction[1]
            if (y < minrow) or (y > maxrow) or (x < minseat) or (x > maxseat):
                foundseat = 1
            else:
                if seatdata[y][x] == "L":
                    foundseat = 1
                elif seatdata[y][x] == "#":
                    adjacent += 1
                    foundseat = 1
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
                adjacent = checkseat(rowindex, seatindex, inputdata)
                if seat == "L":
                    if adjacent == 0:
                        newseats[rowindex] += "#"
                    else:
                        newseats[rowindex] += "L"
                if seat == "#":
                    if adjacent >= seatcount:
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
        samesies = (newdata == inputdata)
        inputdata = copy.copy(newdata)
    
    return countoccupied(newdata)


  

print(checkeverything(inputfile_source))