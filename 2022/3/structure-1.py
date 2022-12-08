#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def splitsack(itemlist):
    itemlength = int(len(itemlist)/2)
    return [itemlist[0:itemlength],itemlist[itemlength:]]

def findshared(rucksacks):
    shared = ""
    for rucksack in rucksacks:
        sharedsack = ""
        for ch in rucksack[0]:
            if ch in rucksack[1] and not ch in sharedsack:
                print(ch)
                sharedsack += ch
        shared += sharedsack
    return shared

def prioritize(items):
    priority = 0
    for item in items:
        if ord(item) > 96:
            #lowercase
            priority += ord(item) - 96
        else:
            #uppercase
            priority += ord(item) - 38
    return priority

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")
    rucksacks = []
    # score = 0
    for line in inputdata:
        rucksacks.append(splitsack(line))
    shareditems = findshared(rucksacks)
    priority = prioritize(shareditems)
    print(rucksacks)
    print(shareditems)
    print(priority)
    #print("Result %s" % sum(thrown))

checkeverything(inputfile_source)