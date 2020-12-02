#!/usr/bin/python

print "importing"

inputfile_source = "2015/1/input.txt"

def floorcount(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    floor = 0
    count = 0
    for item in inputdata[0]:
        count += 1
        if (item == "("):
            floor += 1
        elif (item == ")"):
            floor -= 1
        if (floor == -1):
            print(count)
            return


        
floorcount(inputfile_source)