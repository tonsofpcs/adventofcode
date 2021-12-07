#!/usr/bin/python
import os
import re
import statistics


print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"
forcelocation = -1

def cost_distance(distance):
    distance = abs(distance)
    cost = 0
    for index in range(distance+1):
        cost += index

    #print("Distance %s = Cost %s" % (distance,cost))
    return cost

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    crabs = list(map(int, inputdata[0].split(",")))
    maxcrabs = max(crabs)

    print(statistics.median(crabs))
    print(statistics.mean(crabs))

    if forcelocation == -1:
        # averagecrab = int(statistics.median(crabs)) #part1
        averagecrab = int(statistics.mean(crabs)) #part2
    else:
        averagecrab = forcelocation

    crabdistance = 0
    cost = 0

    for index in range(maxcrabs+1):
        crabdistance += abs(crabs.count(index)*(averagecrab - index))
        cost += abs(crabs.count(index)*cost_distance(averagecrab - index))
    
    print("Distance %s" % crabdistance)
    print("Cost %s" % cost)

checkeverything(inputfile_source)