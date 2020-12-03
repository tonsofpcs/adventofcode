#!/usr/bin/python

print "importing"

inputfile_source = "2020/3/input.txt"

def ski(filename, x, y):
    trees = 0

    inputfile = open(filename)
    inputdata = inputfile.readlines()
    maxlen = (len(inputdata[0]) - 1)
    pos = 0
    items = iter(inputdata)
    next(items)
    for iterat, item in enumerate(items):
        if (((iterat - 1) % y) == 0):
            pos += x
            if (pos > maxlen - 1): 
                pos = pos - maxlen
            if (item[pos] == "#"):
                trees += 1
                
    return trees

print(ski(inputfile_source, 1, 1))        
print(ski(inputfile_source, 1, 2))
print(ski(inputfile_source, 1, 1)*ski(inputfile_source, 3, 1)*ski(inputfile_source, 5, 1)*ski(inputfile_source, 7, 1)*ski(inputfile_source, 1, 2))