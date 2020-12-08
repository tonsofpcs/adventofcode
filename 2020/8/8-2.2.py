#!/usr/bin/python
import os
import copy

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def codeexec(code):
    maxline = len(code)
    acc = 0
    line = 0
    hasrun = []
    success = 1

    while line < maxline:
        command = code[line][0]
        argv = code[line][1]
        if line in hasrun:
            success = 0
            break
        else:
            hasrun.append(line)
        #print(command, argv)
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
    
    if success:
        return acc
    else:
        return 0

def codefix(code):
    result = 0
    line = 0
    length = len(code)
    while (result == 0) and (line <= length):
        code2 = copy.deepcopy(code)
        command = code2[line][0]
        argv = code2[line][1]
        if (command == "nop") and (argv != 0):
            code2[line][0] = "jmp"
            print("Trying to replace nop with jmp on line", line)
            result = codeexec(code2)
        elif (command == "jmp"):
            code2[line][0] = "nop"
            print("Trying to replace jmp with nop on line", line)
            result = codeexec(code2)
        line += 1

    print("result: ", result)
    return result

def checkeverything(filename):
    code = []
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    #get code
    for line in inputdata:
        command = line[0:3]
        argv = int(line[4:])
        code.append([command,argv])

    print("Code loaded")

    return codefix(code)
    #print(code)

print(checkeverything(inputfile_source))