#!/usr/bin/python
import os
import copy
import re

print("importing")


inputfile_source = os.path.dirname(__file__) + "/input.txt"

def splitvalues(dataline):
    splitval = re.split(",|-",dataline,3)
    # print(splitval)
    return list(map(int,splitval))

def findsupersets(pairs):
    supersets = 0
    for pair in pairs:
        supersets += findsuperset(pair)
    return supersets

def findsuperset(pair):
    [min1,max1,min2,max2] = pair
    if ((max1 >= max2) and (min1 <= min2)) or ((max1 <= max2) and (min1 >= min2)):
        # print(pair)
        return 1
    else:
        return 0

def findoverlaps(pairs):
    overlaps = 0
    for pair in pairs:
        overlaps += findoverlap(pair)
    return overlaps

def findoverlap(pair):
    [min1,max1,min2,max2] = pair
    if ((max1 >= min2) and (max1 <= max2)) or ((max2 >= min1) and (max2 <= max1)):
        # print(pair)
        return 1
    else:
        return 0

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    pairs = []
    supersets = 0
    for line in inputdata:
        pairs.append(splitvalues(line)) #min1 max1 min2 max2
    supersets = findsupersets(pairs)
    overlaps = findoverlaps(pairs)
        #result3 = findgroup(line)
    # print(pairs)
    # print("Result %s" % sum(thrown))
    print(supersets)
    print(overlaps)

checkeverything(inputfile_source)