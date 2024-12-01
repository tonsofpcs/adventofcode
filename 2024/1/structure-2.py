#!/usr/bin/python
import os
import copy
import operator


print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    # print(inputdata)

    col1 = []
    col2 = []
    cols = []
    for lineitem in inputdata:
        cols = lineitem.split("   ")
        col1.append(int(cols[0]))
        col2.append(int(cols[1]))
    col1.sort()
    col2.sort()

    # print(col1)
    # print(col2)
    col3 = list(map(operator.sub, col1, col2))
    col4 = list(map(operator.abs,col3))

    listscore = 0

    for lineitem in col1:
        score = col2.count(lineitem)
        listscore += score * lineitem


    print("Result 1: %s" % sum(col4))
    print("Result 2: %s" % listscore)

checkeverything(inputfile_source)