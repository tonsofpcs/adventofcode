#!/usr/bin/python
import os
import copy
import math

debugmode = False
if debugmode: print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

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
    # don't get too smart
    #
    # elif (fullsum < result and fullmult < result) or fullsum > result:
    #     if debugmode: print("Not in range")
    #     return 0
    else:
        # ok let's do some math
        if debugmode: print(len(operands), " operands")
        testmax = pow(3,(len(operands) - 1))-1
        if debugmode: print("Testing", testmax)
        for testcase in range (1, testmax): # check from 00...01 to 2222221 [we already checked all 0s and all 1s]
            testmath = ternary(testcase)
            if debugmode: print(testmath, ternary(testmax))
            # testmath = [testcase >> i & 1 for i in range(len(operands) - 2,-1,-1)]
            if debugmode: print(testmath)
            for tomath,item in enumerate(operands):
                if debugmode: print("Iterate: ", tomath, item)
                if tomath == 0:
                    testresult = operands[0]
                elif testmath[tomath-1] == 0:
                    testresult = testresult + item
                elif testmath[tomath-1] == 1:
                    testresult = testresult * item
                elif testmath[tomath-1] == 2:
                    # testresult = testresult * item
                    # uh... we need to work backwards.  
                else:
                    print("ERROR")
                    return 0
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