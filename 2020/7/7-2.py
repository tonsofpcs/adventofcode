#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"

nothere = []

def checkeverything(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    bags = []

    searchbagcolors = ["shiny gold"]
    searchbagcounts = [1]
    searchbags = [searchbagcolors, searchbagcounts]

    
    print("Parsing data")
    for line in inputdata:
        line = line.replace("bags","bag").replace(" bag, ", "|").replace(" bag contain no other bag.","").replace(" bag contain ","|").replace(" bag.","").replace("\n","")
        lineitems = line.split("|")
        colors = []
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
    
    lenwatch = len(searchbagcolors)
    print("Bags remaining to search:",lenwatch)
    bagcount = 0
    while lenwatch > 0:
        searchnextcolors = []
        searchnextcounts = []
        print(searchbags)
        for lineitems in bags:
            for index, item in enumerate(lineitems):
                if index > 0:
                    if lineitems[0] in searchbagcolors:
                        #print(lineitems[0])
                        #print(item)
                        searchnextcounts.append(item[0]*searchbagcounts[searchbagcolors.index(lineitems[0])])
                        searchnextcolors.append(item[1])
                        bagcount += item[0]*searchbagcounts[searchbagcolors.index(lineitems[0])]
        searchnext = [searchnextcolors, searchnextcounts]
        #print(searchnext, bagcount, len(searchnext))
        #break
        searchbagcolors = list(searchnextcolors)
        searchbagcounts = list(searchnextcounts)
        searchbags = [searchbagcolors, searchbagcounts]
        lenwatch = len(searchbagcolors)
        print("Count so far", bagcount, "Bags remaining to search:",lenwatch)
    print(searchbags)
   

    return (bagcount)

    

print(checkeverything(inputfile_source))