#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

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

    linelen = len(inputdata[0])
    linecount = len(inputdata)
    colsum = []
    epsilon = []
    gamma = []
    for col in range(linelen):
        colsum.append(0)
        for line in inputdata:
            colsum[col] += int(line[col])
        print(colsum[col])
        gamma.append(str(1*(colsum[col] > linecount/2)))
        epsilon.append(str(1*(colsum[col] <= linecount/2)))
    
    print(gamma)
    print(epsilon)

    epstot = int(''.join(epsilon), 2)
    gamtot = int(''.join(gamma), 2)
    mult = epstot*gamtot

    print("Epsilon %s" % epstot)
    print("Gamma %s" % gamtot)
    print("Mult %s" % mult)

checkeverything(inputfile_source)