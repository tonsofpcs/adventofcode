#!/usr/bin/python
import os
import re
import statistics


print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"
costincrement = 3
forcelocation = -1

def cost_distance(distance):
    distance = abs(distance)
    cost = 0
    for index in range(distance+1):
        cost += index

    print("Distance %s = Cost %s" % (distance,cost))
    return cost

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    crabs = list(map(int, inputdata[0].split(",")))
    maxcrabs = max(crabs)
    #abstractcrabs = [0]*(maxcrabs+1)
    
    #crabsum = 0

    #for index in range(maxcrabs+1):
    #    abstractcrabs[index] = crabs.count(index)
    #    crabsum += index * abstractcrabs[index]

    print(statistics.median(crabs)) #crabsum*1.0/maxcrabs)
    #averagecrab = int(crabsum/maxcrabs)

    if forcelocation == -1:
        averagecrab = int(statistics.median(crabs))
    else:
        averagecrab = forcelocation

    crabdistance = 0
    cost = 0

    #for index, location in enumerate(abstractcrabs):
    for index in range(maxcrabs+1):
        crabdistance += abs(crabs.count(index)*(averagecrab - index))
        cost += abs(crabs.count(index)*cost_distance(averagecrab - index))
    
    print("Distance %s" % crabdistance)
    print("Cost %s" % cost)
    #print("Result %s" % result3)

checkeverything(inputfile_source)