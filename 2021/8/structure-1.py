#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findnumbers(dataset):
    seekvalue = 0
    # for item in testrange:
    #     seekvalue = 1
    return seekvalue

def readline(line):
    fulldataset = []
    rawoutput = []
    rawoutput = line[line.find("|")+2:].split(" ")
    fulldataset = line.split(" ")
    fulldataset.remove('|')
    return fulldataset, rawoutput

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    for line in inputdata:
        dataset,raw = readline(line)
        result3 = findnumbers(dataset)

        print("Dataset: %s" % dataset)
        print("Raw Out: %s" % raw)
        print("Numbermap: %s" % result3)

checkeverything(inputfile_source)