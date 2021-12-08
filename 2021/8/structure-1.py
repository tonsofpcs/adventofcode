#!/usr/bin/python
import os
import copy
import re

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

# nummap = {
#     #[0,0,0,0,0,0,0]: -1,
#     [1,1,1,0,1,1,1]: 0,
#     [0,0,1,0,0,1,0]: 1,
#     [1,0,1,1,1,0,1]: 2,
#     [1,0,1,1,0,1,1]: 3,
#     [0,1,1,1,0,1,0]: 4,
#     [1,1,0,1,0,1,1]: 5,
#     [1,1,0,1,1,1,1]: 6,
#     [1,0,1,0,0,1,0]: 7,
#     [1,1,1,1,1,1,1]: 8,
#     [1,1,1,1,0,1,1]: 9
# }

def possiblekeep(possibilities, whattokeep):
    # print("Old: %s" % possibilities)
    # print("Keep: %s" % whattokeep)
    newposs = ""
    return newposs.join(re.findall("[" + whattokeep + "]", possibilities))    

def possibleremove(possibilities, whattokeep):
    # print("Old: %s" % possibilities)
    # print("Keep: %s" % whattokeep)
    return re.sub("[" + whattokeep + "]", "", possibilities)

def findnumbers(dataset):
    wirepossibilities = ["abcdefg"]*7
    for wireset in dataset:
        #print(wirepossibilities)
        numwires = len(wireset)
        if numwires >= 7:  #EIGHT, tells us nothing for the map
            continue
        elif numwires == 2:  #ONE, 3+6
            for wireid in range(7):
                if wireid in [2,5]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                else:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        elif numwires == 3:  #SEVEN, 1+3+6
            for wireid in range(7):
                if wireid in [2, 5, 0]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                else:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        elif numwires == 4:  #FOUR, 2+3+4+6
            for wireid in range(7):
                if wireid in [1, 2, 3, 5]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                else:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        elif numwires == 5:  #two, three, five - tells nothing on its own
            continue
        elif numwires == 6:  #zero, six, nine - tells nothing on its own
            continue
    for wireset in dataset:
        #print(wirepossibilities)
        numwires = len(wireset)
        if numwires >= 7:  #EIGHT, tells us nothing for the map
            continue
        elif numwires <= 4:  #one, seven, four - already done
            continue
        elif numwires == 5:  #two, three, five
            # if x in wirepossibilities[1]
            continue
        elif numwires == 6:  #zero, six, nine
            continue
    return wirepossibilities


def readline(line):
    fulldataset = []
    rawoutput = []
    rawoutput = line[line.find("|")+2:].split(" ")
    fulldataset = line.split(" ")
    fulldataset.remove('|')
    return fulldataset, rawoutput

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    for line in inputdata:
        dataset,raw = readline(line)
        numbermap = findnumbers(dataset)


        print("Dataset: %s" % dataset)
        print("Raw Out: %s" % raw)
        print("Numbermap: %s" % numbermap)

checkeverything(inputfile_source)