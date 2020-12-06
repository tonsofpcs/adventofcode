#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

lettermap = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for index, c in enumerate(alphabet):
    lettermap[c] = index

def orlist(list1, list2):
    return [l1 | l2 for l1,l2 in zip(list1,list2)]

def andlist(list1, list2):
    return [l1 & l2 for l1,l2 in zip(list1,list2)]

def checkperson(person):
    #test = [1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,2,1,2,3,4,5,6]
    #test = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    test = [False] * 26
    if len(person) > 0:
        for c in person:
            test[lettermap.get(c)] = 1
        #print(test)
        return test

def checkgroup(testgroup):
    test = [True] * 26
    persons = testgroup.split("\n")
    for person in persons:
        test = andlist(test, checkperson(person))
    print(sum(test))
    return test

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n\n")
    test = 0
    for group in inputdata:
        test = test + sum(checkgroup(group))
    #testsum = sum(test)
    print("Result %s" % test)

checkeverything(inputfile_source)