#!/usr/bin/python

print "importing"

inputfile_source = "2020/2/input.txt"

def passwordcheck(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines().split(" ")
    inputdata1 = inputdata[1]
    inputdata2 = inputdata[2]
    inputdata3 = inputdata[3]
    print(inputdata1)
