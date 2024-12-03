#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findvalues(testrange):
    # check for validity, output values to multiply
    seekvalue = []
    testrange = testrange[1:]
    testrange = testrange.split(",")
    try:
        teststr = str(int(testrange[0]))
    except:
        return [0,0]
    if teststr == testrange[0]:
        seekvalue.append(int(testrange[0]))
    else:
        return [0,0]
    testrange = testrange[1].split(")")
    try:
        teststr = str(int(testrange[0]))
    except:
        return [0,0]
    if teststr == testrange[0]:
        seekvalue.append(int(testrange[0]))
    else:
        return [0,0]
    # print(seekvalue)
    return seekvalue

    

def processvalues(testrange):
    # multiply values
    return testrange[0] * testrange[1]

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    if inputfiledata[0-3] == "mul":
        offset = 0
    else:
        offset = 1
    inputdata = inputfiledata.split("mul")
    if offset == 1:
        del inputdata[0]
    multipliers = [0,0]
    product = 0
    summation = 0
    for line in inputdata:
        multipliers = findvalues(line)
        product = processvalues(multipliers)
        summation += product
    # print("Result %s" % multipliers)
    print("Result %s" % product)
    print("Result %s" % summation)

checkeverything(inputfile_source)