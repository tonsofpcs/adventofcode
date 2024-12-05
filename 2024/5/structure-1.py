#!/usr/bin/python
import os
import copy

debugmode = True

if debugmode: print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def checkcorrect(testrange,rules):
    for ruleitem in rules:
        if ruleitem[0] in testrange and ruleitem[1] in testrange:
            if testrange.index(ruleitem[0]) > testrange.index(ruleitem[1]):
                return -1
    if debugmode: print("Correct:", testrange)
    return testrange

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (checkcorrect(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    afterblank = 0
    pagerules = []
    updates = []
    for linenum,line in enumerate(inputdata):
        if(line == ""):
            afterblank = 1
        elif afterblank:
            updates.append(line.split(','))
        else:
            pagerules.append(line.split('|'))

    if debugmode: print(pagerules)
    if debugmode: print("########")
    if debugmode: print(updates)
    if debugmode: print("########")

    middlevalue = 0
    for line in updates:
        correct = checkcorrect(line,pagerules)
        if not(correct == -1):
            middlevalue += int(correct[int(len(correct)/2)])

    #     result2 = findthing2(line)
    #     result3 = findgroup(line)
    print("Result %s" % middlevalue)
    # print("Result %s" % result3)

checkeverything(inputfile_source)