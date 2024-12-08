#!/usr/bin/python
import os
import copy
import math

debugmode = True
if debugmode: print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findthing1(testrange):
    if debugmode: print("Test range:", testrange)
    [result, operands] = testrange.split(": ")
    result = int(result)
    operands = list(map(int, operands.split(" ")))
    fullsum = sum(operands)
    fullmult = math.prod(operands)
    if fullsum == result or fullmult == result:
        if debugmode: print("Full sum or mult matched")
        return result
    elif (fullsum < result and fullmult < result) or fullsum > result:
        if debugmode: print("Not in range")
        return 0
    else:
        # ok let's do some math
        if debugmode: print(len(operands), " operands")
        testmax = pow(2,(len(operands) - 1))-1
        if debugmode: print("Testing", testmax)
        for testcase in range (1, testmax): # check from 00...01 to 11111110 [we already checked all 0s and all 1s]
            if debugmode: print(bin(testcase), bin(testmax))
            testmath = [testcase >> i & 1 for i in range(len(operands) - 2,-1,-1)]
            if debugmode: print(testmath)
            for tomath,item in enumerate(operands):
                if debugmode: print("Iterate: ", tomath, item)
                if tomath == 0:
                    testresult = operands[0]
                elif testmath[tomath-1] == 0:
                    testresult = testresult + item
                else:
                    testresult = testresult * item
            if testresult == result:
                return result
            if debugmode: print(testresult)
    return 0
    
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
    result1 = 0
    for line in inputdata:
        result1 += findthing1(line)
        # result2 = findthing2(line)
        # result3 = findgroup(line)
    if debugmode: print("Result %s" % result1)
    # if debugmode: print("Result %s" % result2)
    # if debugmode: print("Result %s" % result3)
    return result1

print(checkeverything(inputfile_source))