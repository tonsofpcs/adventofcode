#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

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
#startdir = 0

def moveit(startpos, direction, amt):
    for index, item in enumerate(startpos):
        startpos[index] += direction[index] * amt
    return startpos

def rotatetarget(target, base, direction, times):
    reference = copy.copy(target)
    while times > 4:
        times -= 4 #let's not do this more than we have to
    reference[0] = target[0]
    reference[1] = target[1]
    holder = 0
    while times > 0:
        holder = reference[0]
        reference[0] = reference[1]*direction
        reference[1] = holder*(0-direction)
        times -= 1
    return reference


def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    #facing = startdir
    position = [0,0]
    waypoint = [10,1]
    for line in inputdata:
        order = line[0]
        argv = int(line[1:])
        if order in ["N","S","E","W"]:
            movement = cardinal.get(order)
            waypoint = moveit(waypoint, directions.get(movement), argv)
        elif order in ["L","R"]:
            waypoint = rotatetarget(waypoint, position, turn.get(order), argv/90)
        elif order == "F":
            position = moveit(position, waypoint, argv)
        else:
            print("ERROR! " + order + " is not a valid order!")
        #print(position,waypoint)
        
    print(position, waypoint)
    print("Manhattan distance: %s" % (abs(position[0])+abs(position[1])))

print checkeverything(inputfile_source)