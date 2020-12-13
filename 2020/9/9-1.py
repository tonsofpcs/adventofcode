#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"
testlength = 25

def testpair(testrange, sumtocheck):
    success = 0
    for item in testrange:
        for item2 in testrange:
            if (int(item.replace("\n","")) + int(item2.replace("\n",""))) == int(sumtocheck):
                success = 1
                break
    return success

def checkeverything(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for index, line in enumerate(inputdata):
        if index >= testlength:
            success = testpair(inputdata[index-(testlength):index],line)
            if not(success): break
    
    return line

print(checkeverything(inputfile_source))