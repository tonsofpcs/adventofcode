#!/usr/bin/python

print "importing"

inputfile_source = "2020/3/input.txt"

def ski(filename):
    countgood = 0
    countbad = 0
    counterr = 0
    count = 0

    inputfile = open(filename)
    inputdata = inputfile.readlines()
    maxlen = (len(inputdata[0]) - 1)
    print("maxlen: %s" % maxlen)
    pos = 0
    items = iter(inputdata)
    next(items)
    for item in items:
        pos += 3
        if (pos > maxlen - 1): 
            pos = pos - maxlen
        if (item[pos] == "#"):
            countbad += 1
        elif (item[pos] == "."):
            countgood += 1
        else:
            counterr += 1
        count += 1
        
    print("count good: %s" % countgood)
    print("count bad: %s" % countbad)
    print("error: %s" % counterr)
    print("count: %s" % count)
    print("total: %s" % (countgood+countbad))
        
ski(inputfile_source)