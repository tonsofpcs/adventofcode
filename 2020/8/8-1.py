#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def codeexec(code):
    maxline = len(code)
    acc = 0
    line = 0
    hasrun = []

    while line < maxline:
        command = code[line][0]
        argv = code[line][1]
        if line in hasrun:
            break
        else:
            hasrun.append(line)
        print(command, argv)
        if (command == "acc"):
            acc += argv
            line += 1
        elif (command == "jmp"):
            line += argv
        elif (command == "nop"):
            line += 1
        else:
            print("Error!  Command unknown.", command, argv)
            break

    return acc

def checkeverything(filename):
    code = []
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    #get code
    for line in inputdata:
        command = line[0:3]
        argv = int(line[4:])
        code.append([command,argv])
    return codeexec(code)
    #print(code)

print(checkeverything(inputfile_source))