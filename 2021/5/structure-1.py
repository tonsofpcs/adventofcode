#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def inlinehv (point, path):
    if (point[1] == path[0][1] == path[1][1]) and ((path[0][0] <= point[0] <= path[1][0]) or (path[0][0] >= point[0] >= path[1][0])):
        #print(point,path,"H")
        return(True)
    elif (point[0] == path[0][0] == path[1][0]) and ((path[0][1] <= point[1] <= path[1][1]) or (path[0][1] >= point[1] >= path[1][1])):
        #print(point,path,"V")
        return(True)
    else:
        return(False)

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    paths = []
    hvpaths = []

    grid = []
    for x in range(1000):
        gridrow = []
        for y in range(1000):
            gridrow.append(0)
        grid.append(gridrow)
    #print(grid)

    for line in inputdata:
        x1,y1 = line.split(" -> ")[0].split(",")
        x2,y2 = line.split(" -> ")[1].split(",")
        paths.append([[int(x1),int(y1)],[int(x2),int(y2)]])
        if (x1 == x2) or (y1 == y2):
            hvpaths.append([[int(x1),int(y1)],[int(x2),int(y2)]])
    
    ge2 = 0
    item = 0
    pathlen = len(hvpaths)
    for path in hvpaths:
        item += 1
        print("%s of %s" % (item, pathlen))
        xmin = min(path[0][0],path[1][0])
        xmax = max(path[0][0],path[1][0])
        ymin = min(path[0][1],path[1][1])
        ymax = max(path[0][1],path[1][1])
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                if inlinehv([x,y],path):
                    grid[y][x] += 1
                    #print(x,y,grid[y][x])
                    if grid[y][x] == 2:
                        ge2 += 1  


    #print("All lines:")
    #print(paths)
    #print("HV Only:")
    #print(hvpaths)

    print("Result %s" % ge2)
    #print(grid)

checkeverything(inputfile_source)