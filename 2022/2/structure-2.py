#!/usr/bin/python
import os
import copy

print("importing")

pointsmap = {
    'A': 1,
    'B': 2,
    'C': 3
}

win = 6
tie = 3
lose = 0

# AX rock
# BY paper
# CZ scissors

throwmap = {
    'A X': 'C',
    'A Y': 'A',
    'A Z': 'B',
    'B X': 'A',
    'B Y': 'B',
    'B Z': 'C',
    'C X': 'B',
    'C Y': 'C',
    'C Z': 'A'
}

winmap = {
    'X': lose,
    'Y': tie,
    'Z': win,
}

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findscore(testrange):
    score = 0
    score += winmap[testrange[2]]
    #print(score)
    score += pointsmap[throwmap[testrange]]
    #print(score)
    #print(testrange, " : ", testrange[2])
    return score

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (findscore(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    thrown = []
    score = 0
    for line in inputdata:
        thrown.append(findscore(line))
        #result2 = findthing2(line)
        #result3 = findgroup(line)
    print(thrown)
    print("Result %s" % sum(thrown))

checkeverything(inputfile_source)