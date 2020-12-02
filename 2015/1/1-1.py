#!/usr/bin/python

print "importing"

inputfile_source = "2015/1/input.txt"

def floorcount(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    up = 0
    down = 0
    for item in inputdata[0]:
        if (item == "("):
            up += 1
        elif (item == ")"):
            down += 1
    print("up %s, down %s, net %s", up, down, (up-down))

        
floorcount(inputfile_source)