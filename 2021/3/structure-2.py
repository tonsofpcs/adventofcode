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
    #linecount = len(inputdata)

    colsum = []
    gamma = []
    gamtot = ""
    for col in range(linelen):
        linecount = 0 
        colsum.append(0)
        for line in inputdata:
            if (gamtot == "") or (line[0:len(gamtot)] == gamtot):
                print("Gamtot %s , line %s" % (gamtot, line))
                colsum[col] += int(line[col])
                linecount += 1
        if linecount == 1:
            break
        print(colsum[col], linecount/2.0,str(1*(colsum[col] >= linecount/2.0)))
        gamma.append(str(1*(colsum[col] >= linecount/2.0)))
        gamtot = ''.join(gamma)
        print(gamtot)

    #find that last one
    for line in inputdata:
        if (line[0:len(gamtot)] == gamtot):
            gamtot = line
            break
    
    print("Oxygen %s : %s" % (gamtot, int(gamtot,2)))
    gamtot = int(gamtot,2)

    colsum = []
    epsilon = []
    epstot = ""
    for col in range(linelen):
        linecount = 0 
        colsum.append(0)
        for line in inputdata:
            if (epstot == "") or (line[0:len(epstot)] == epstot):
                print("Epstot %s , line %s" % (epstot, line))
                colsum[col] += int(line[col])
                linecount += 1
        if linecount == 1:
            break
        print(colsum[col], linecount/2.0,str(1*(colsum[col] < linecount/2.0)))
        epsilon.append(str(1*(colsum[col] < linecount/2.0)))
        epstot = ''.join(epsilon)
        print(epstot)

    #find that last one
    for line in inputdata:
        if (line[0:len(epstot)] == epstot):
            epstot = line
            break

    print("CO2 %s : %s" % (epstot, int(epstot,2)))
    epstot = int(epstot,2)






    print(gamma, epsilon)

    #epstot = int(''.join(epsilon), 2)
    #gamtot = int(''.join(gamma), 2)
    mult = epstot*gamtot

    print("Epsilon %s" % epstot)
    print("Gamma %s" % gamtot)
    print("Mult %s" % mult)

checkeverything(inputfile_source)