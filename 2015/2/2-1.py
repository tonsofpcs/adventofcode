#!/usr/bin/python

print "importing"

inputfile_source = "2015/2/input.txt"

def elves(filename):
    dimensions = []
    totalpaperneed = 0
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for item in inputdata:
        dataset = item.split("x")
        l = int(dataset[0])
        w = int(dataset[1])
        h = int(dataset[2])
        smallside = l*w
        if ((w*h) < smallside):
            smallside = w*h
        if ((l*h) < smallside):
            smallside = l*h
        paperneed = 2*(l*w)+2*(l*h)+2*(w*h)+smallside
        dimensions.append([l, w, h, paperneed])
        totalpaperneed += paperneed
    print("total: %s", (totalpaperneed))
        
elves(inputfile_source)