#!/usr/bin/python
import os
import copy
import re

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

tocount = [1,4,7,8]

nummap = {
    #[0,0,0,0,0,0,0]: -1,
    '012456': 0,
    '25': 1,
    '02346': 2,
    '02356': 3,
    '1235': 4,
    '01356': 5,
    '013456': 6,
    '025': 7,
    '0123456': 8,
    '012356': 9
}

# maptable = ['a','b','c','d','e','f','g']
maptable = ['0','1','2','3','4','5','6']

def possiblekeep(possibilities, whattokeep):
    # print("Old: %s" % possibilities)
    # print("Keep: %s" % whattokeep)
    newposs = ""
    return newposs.join(re.findall("[" + whattokeep + "]", possibilities))    

def possibleremove(possibilities, whattokeep):
    # print("Old: %s" % possibilities)
    # print("Keep: %s" % whattokeep)
    return re.sub("[" + whattokeep + "]", "", possibilities)

def possiblecontain(possibilities, searchfor):
    return bool(re.search("[" + searchfor + "]", possibilities))
    # find = possibilities.find(searchfor)
    # return (find != -1)

def possiblecontainall(possibilities, containin):
    # print("Testall %s : %s" % (containin, possibilities))
    result = True
    for item in possibilities:
        test = (containin.find(item) != -1)
        result = result & test
    return result



def findnumbers(dataset):
    wirepossibilities = ["abcdefg"]*7
    dataset.sort(key=len)

    wireset = dataset[0] #length 2
    # elif numwires == 2:  #ONE, 3+6
    for wireid in range(7):
        if wireid in [2,5]:
            wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
        else:
            wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    wireset = dataset[1] #length 3
    # elif numwires == 3:  #SEVEN, 1+3+6
    for wireid in range(7):
        if wireid in [0, 2, 5]:
            wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
        else:
            wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    wireset = dataset[2] #length 4
    # elif numwires == 4:  #FOUR, 2+3+4+6
    for wireid in range(7):
        if wireid in [1, 2, 3, 5]:
            wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
        else:
            wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    for wireset in dataset[6:9]: #6 long, that gives us 6, 9, and 0.
        if not possiblecontainall(wirepossibilities[2],wireset): #SIX #wirepossibilities 2 and 5 should match until this point
            # print("Six! %s" % wireset)
            for wireid in range(7):
                if wireid in [0,1,3,4,6]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                elif wireid == 2:  # 2 and 5
                    wirepossibilities[2] = possibleremove(wirepossibilities[2],wireset)
                elif wireid == 5:
                    wirepossibilities[5] = possibleremove(wirepossibilities[5],wirepossibilities[2])
            # print(wirepossibilities)
    for wireset in dataset[3:6]: #5 long, that gives us 2, 5, and 3.  We should be able to identify them all.  
        if possiblecontain(wirepossibilities[2],wireset) and possiblecontain(wirepossibilities[4],wireset) and (not(possiblecontain(wirepossibilities[5],wireset))): #TWO!
            # print("Two! %s" % wireset)
            for wireid in range(7):
                if wireid in [0,2,3,4,6]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                elif wireid in [1,5]:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        elif possiblecontain(wirepossibilities[1],wireset) and possiblecontain(wirepossibilities[5],wireset) and (not(possiblecontain(wirepossibilities[2],wireset))): #FIVE!
            # print("Five! %s" % wireset)
            for wireid in range(7):
                if wireid in [0,1,3,5,6]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                elif wireid in [2,4]:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        elif possiblecontain(wirepossibilities[2],wireset) and possiblecontain(wirepossibilities[5],wireset): #THREE!
            # print("Three! %s" % wireset)
            for wireid in range(7):
                if wireid in [0,2,3,5,6]:
                    wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
                elif wireid in [1,4]:
                    wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
        else:
            print("Five wires but not 2,3,5?")


        #print(wirepossibilities)
    #     numwires = len(wireset)
    #     if numwires >= 7:  #EIGHT, tells us nothing for the map
    #         continue
    #     elif numwires <= 4:  #one, seven, four - already done
    #         continue
    #     elif numwires == 5:  #two, three, five
    #     elif numwires == 6:  #zero, six, nine
    #         if not possiblecontain(wirepossibilities[3],wireset): #ZERO
    #             print("Zero! %s" % wireset)
    #             for wireid in range(7):
    #                 if wireid in [0,1,2,4,5,6]:
    #                     wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
    #                 # elif wireid == 3:  #already there if we matched
    #                 #     wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    #         elif not possiblecontainall(wirepossibilities[2],wireset): #SIX #wirepossibilities 2 and 5 should match until this point
    #             print("Six! %s" % wireset)
    #             for wireid in range(7):
    #                 if wireid in [0,1,3,4,5,6]:
    #                     wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
    #                 # elif wireid == 2:  #already there if we matched
    #                 #     wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    #         elif not possiblecontain(wirepossibilities[4],wireset): #NINE
    #             print("Nine! %s" % wireset)
    #             for wireid in range(7):
    #                 if wireid in [0,1,2,3,5,6]:
    #                     wirepossibilities[wireid] = possiblekeep(wirepossibilities[wireid],wireset)
    #                 # elif wireid == 4:  #already there if we matched
    #                 #     wirepossibilities[wireid] = possibleremove(wirepossibilities[wireid],wireset)
    #         else:
    #             print("Six wires but inconclusive. %s : %s" % (wireset, wirepossibilities))
    # # check if any are single characters, remove from others

    return wirepossibilities


def readline(line):
    fulldataset = []
    rawoutput = []
    rawoutput = line[line.find("|")+2:].split(" ")
    fulldataset = line.split(" ")[:10] #the first 10
    #fulldataset.remove('|')
    return fulldataset, rawoutput

def mapdata(dataset, numbermap):
    datamap = dict(zip(numbermap, maptable))
    mapdataset = []
    print(datamap)
    for item in dataset:
        # print(item)
        newitem = [datamap.get(res) for res in list(item)]
        newitem.sort()
        newitem = ''.join(newitem)
        # print(newitem)
        mapdataset.append(newitem)
    print("Map data: %s" % mapdataset)
    return mapdataset

def display(characterset):
    displayval = []
    for char in characterset:
        displayval.append(nummap[char])
    return displayval

def countem(whattocount):
    count = 0
    for item in tocount:
        count += whattocount.count(item)
    return count

def largenum(whattosum):
    return whattosum[0]*1000+whattosum[1]*100+whattosum[2]*10+whattosum[3]

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    countthem = 0
    sumthem = 0

    for line in inputdata:
        dataset,raw = readline(line)
        numbermap = findnumbers(dataset)
        nums = display(mapdata(raw, numbermap))
        countthem += countem(nums)
        sumthem += largenum(nums)

        # lenset = []
        # for line in dataset:
        #     lenset.append(len(line))

        print("Dataset: %s" % dataset)
        # print("Lengths: %s" % lenset)
        print("Raw Out: %s" % raw)
        print("Numbermap: %s" % numbermap)
        print("Display: %s" % nums)
   
    print("Count : %s" % countthem)
    print("Sum : %s" % sumthem)

checkeverything(inputfile_source)