#!/usr/bin/python

print "importing"

inputfile_source = "2015/2/input.txt"

def elves(filename):
    dimensions = []
    totalpaperneed = 0
    totalribbonneed = 0
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
        smallperim = perim(l,w)
        if (perim(w,h) < smallperim):
            smallperim = perim(w,h)
        if (perim(l,h) < smallperim):
            smallperim = perim(l,h)
        paperneed = 2*(l*w)+2*(l*h)+2*(w*h)+smallside
        ribbonneed = smallperim+l*w*h
        dimensions.append([l, w, h, paperneed, ribbonneed])
        totalpaperneed += paperneed
        totalribbonneed += ribbonneed
    print("total paper: %s", totalpaperneed)
    print("total ribbon: %s", totalribbonneed)

def perim(side1, side2):
    return (2*side1 + 2*side2)


elves(inputfile_source)