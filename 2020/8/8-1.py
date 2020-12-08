#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def codeexec(code):
    acc = 0
    for [command, argv] in code:
        seekvalue = 1
    return seekvalue

def checkeverything(filename):
    code = []
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    #get code
    for line in inputdata:
        command = line[0:3]
        argv = int(line[4:])
        code.append([command,argv])
    #return codeexec(code)
    print(code)

checkeverything(inputfile_source)