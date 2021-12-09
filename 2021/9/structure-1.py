#!/usr/bin/python
import os
import copy
import sys

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findthing1(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    array = []
    for line in inputdata:
        array.append(list(line))
    
    width = len(array[0])
    height = len(array)
    for y in range(height):
        for x in range(width):
            print(array[y][x], end='')
        print("")

    # print("Result %s" % result1)
    # print("Result %s" % result2)
    # print("Result %s" % result3)

checkeverything(inputfile_source)