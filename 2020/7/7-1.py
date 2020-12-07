#!/usr/bin/python
import os

print "importing"

colors = []
contents = []
inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def checkeverything(filename, testcolor):
    global colors
    global contents
    containerbags = []

    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for line in inputdata:
        line = line.replace("bags", "bag").replace(" bag, ", "|").replace(" bag.","").replace(" bag contain ","|").replace("|no other","").replace("\n","")
        linedata = line.split("|")
        notfound = not(linedata[0] in colors)
        if notfound:
            colors.append(linedata[0])
        else:
            print("Not unique!", linedata[0])
        colorcontents = []
        for index, item in enumerate(linedata):
            if index == 0:
                colorcontents.append(item)
            else:
                colorcontentsitem = item.split(" ",1)
                colorcontents.append([colorcontentsitem[0],colorcontentsitem[1]])
        contents.append(colorcontents)
        #print(colorcontents)
    
    for line in contents:
        #print(line)
        for index, item in enumerate(line):
            if index > 0:
                #print(item)
                if item[1] == testcolor:
                    containerbags.append(line[0])
    return containerbags

#dark orange bags contain 3 bright white bags, 4 muted yellow bags.
#faded blue bags contain no other bags.

print(checkeverything(inputfile_source, "shiny gold"))