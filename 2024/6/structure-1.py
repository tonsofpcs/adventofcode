#!/usr/bin/python
import os
import copy
import math

debugmode = False
if debugmode: print("importing")

def rotateright(starting):
    if starting == [-1,0]: return [0,1]
    elif starting == [0,1]: return [1,0]
    elif starting == [1,0]: return [0,-1]
    elif starting == [0,-1]: return [-1,0]
    else: 
        print("ERROR TURNING THE GUARD")
        return [1,1]

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    direction = [-1,0]
    visited = inputdata.copy()
    if "^" in inputfiledata:
        if debugmode: print("Yay! A guard!")
        guardlocation = inputfiledata.index("^")
        if debugmode: print("Guard at:", guardlocation)
        width = len(inputdata[0])
        height = len(inputdata)
        if debugmode: print("Size:", width, height)
        guardrow = int(math.floor(guardlocation/(width + 1)))  # + 1 to account for \n
        guardcol = int(guardlocation - guardrow * (width + 1))
        guardxy = [guardcol, guardrow]
        if debugmode: print(inputdata[guardrow][guardcol]," at ", guardxy)
        while True:
            visited[guardrow] = visited[guardrow][:guardcol] + 'X' + visited[guardrow][guardcol+1:]
            nextrow = guardrow + direction[0]
            nextcol = guardcol + direction[1]
            if nextcol < 0 or nextrow < 0 or nextcol >= width or nextrow >= height:
                break
            if debugmode: print("Next: ",nextrow,", ", nextcol)
            if inputdata[nextrow][nextcol] == "#":
                direction = rotateright(direction)
            guardrow += direction[0]
            guardcol += direction[1]
        endmap = '\n'.join(visited)
        print(endmap)
        return endmap.count("X")
    else:
        return "Error, Guard not found."
    
print(checkeverything(inputfile_source))