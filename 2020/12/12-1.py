#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

directions = {
    0: [1,0],  #E
    1: [0,-1], #S
    2: [-1,0], #W
    3: [0,1] #N
}

cardinal = {
    "E": 0,
    "S": 1,
    "W": 2,
    "N": 3 #N
}

turn = {
    "R": 1,
    "L": -1,
}

maxdir = 3
startdir = 0

def moveit(startpos, direction, amt):
    for index, item in enumerate(startpos):
        startpos[index] += directions[direction][index] * amt
    return startpos

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    facing = startdir
    position = [0,0]
    for line in inputdata:
        order = line[0]
        argv = int(line[1:])
        if order in ["N","S","E","W"]:
            movement = cardinal.get(order)
            position = moveit(position, movement, argv)
        elif order in ["L","R"]:
            facing = facing + int(turn.get(order) / 90)
            while facing > maxdir:
                facing -= maxdir+1
            while facing < 0:
                facing += maxdir+1
        elif order == "F":
            position = moveit(position, facing, argv)
        else:
            print("ERROR! " + order + " is not a valid order!")
        print(position, facing)
        
    print(position, facing)
    print("Manhattan distance: %s" % (abs(position[0])+abs(position[1])))

print checkeverything(inputfile_source)