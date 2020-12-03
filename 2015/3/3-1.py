#!/usr/bin/python

inputfile_source = "2015/3/input.txt"

def santa(filename):
    house[1000][1000] = 1
    delivered = 1
    unique = 1
    x_index = 0
    y_index = 0
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for item in inputdata[0]:
        if (item == "^"):
            y_index += 1
        elif (item == "v"):
            y_index -= 1
        elif (item == "<"):
            x_index -= 1
        elif (item == ">"):
            x_index += 1
        if not (house[x_index][y_index]):
            location[x_index][y_index] = 1
            unique += 1
        delivered += 1
    print("unique deliveries %s", unique)
    print("total deliveries %s", delivered)


santa(inputfile_source)