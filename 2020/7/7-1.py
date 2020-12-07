#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

colors = []
bags = []
biggerbags = []

bagtype = "shiny gold"

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

def checkeverything(filename, checkfor):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    
    print("Parsing data")
    for line in inputdata:
        line = line.replace("bags","bag").replace(" bag, ", "|").replace(" bag contain no other bag.","").replace(" bag contain ","|").replace(" bag.","").replace("\n","")
        lineitems = line.split("|")
        bag = []
        for index, item in enumerate(lineitems):
            if index == 0:
                colors.append(item)
                bag.append(item)
            else:
                item = item.split(" ",1)
                bag.append([int(item[0]), item[1]])
        bags.append(bag)
    #print(bags)

    print("Checking bags")
    for lineitems in bags:
        #print(lineitems)
        for index, item in enumerate(lineitems):
            if index > 0:
                if item[1] == checkfor:
                    biggerbags.append(lineitems[0])
    return biggerbags

print(checkeverything(inputfile_source, bagtype))