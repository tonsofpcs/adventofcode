#!/usr/bin/python
import os

print "importing"

colors = []
contents = []
inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

nothere = []
validbags = ["shiny gold"]

def checkeverything(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    bags = []
    
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
    
    lenwatch1 = len(bags)
    lenwatch2 = 0
    print(lenwatch1, lenwatch2)
    while not(lenwatch2 == lenwatch1):
        nothere = []
        for lineitems in bags:
            found = 0
            #print(lineitems)
            for index, item in enumerate(lineitems):
                if index > 0:
                    if item[1] in validbags:
                        print(item[1])
                        if not(lineitems[0] in validbags): #don't add if already in the list
                            validbags.append(lineitems[0])
                        found = 1
            if not(found):
                nothere.append(lineitems)  #this removes all bags that don't contain other bags and keeps all bags that didn't contain the bags we searched for
        bags = list(nothere)
        lenwatch2 = lenwatch1
        lenwatch1 = len(bags)
        print("Bags == nothere?", (bags == nothere))
        print(lenwatch1, lenwatch2)
    

    return (validbags, len(validbags) - 1)

    

print(checkeverything(inputfile_source))
