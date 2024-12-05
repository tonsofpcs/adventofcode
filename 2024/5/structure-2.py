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
    # if debugmode: print("Correct:", testrange)
    return testrange

def fixincorrect(testrange,rules):
    while checkcorrect(testrange,rules) == -1:
        for ruleitem in rules:
            if ruleitem[0] in testrange and ruleitem[1] in testrange:
                if testrange.index(ruleitem[0]) > testrange.index(ruleitem[1]):
                    del testrange[testrange.index(ruleitem[0])]
                    testrange = [ruleitem[0]] + testrange
                    break
    #     if debugmode: print("incorrect fix:", testrange)
    # if debugmode: print("incorrect fixed", testrange)
    return testrange
    

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
    incorrectmiddle = 0
    for line in updates:
        correct = checkcorrect(line,pagerules)
        if not(correct == -1):
            middlevalue += int(correct[int(len(correct)/2)])
        else:
            incorrectfix = fixincorrect(line,pagerules)
            incorrectmiddle += int(incorrectfix[int(len(incorrectfix)/2)])

    print("Result 1: %s" % middlevalue)
    print("Result 2: %s" % incorrectmiddle)

checkeverything(inputfile_source)