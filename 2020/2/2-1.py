#!/usr/bin/python

print "importing"

inputfile_source = "2020/2/input.txt"

def passwordcheck(filename):
    data_min = data_max = data_char = data_pass = []
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for item in inputdata:
        dataset = item.split(" ")
        dataset_minmax = dataset[1].split("-")
        data_min.append(dataset_minmax[1])
        data_max.append(dataset_minmax[2])
        data_char.append(dataset[2][:1])
        data_pass.append(dataset[3])
    print(data_char)

passwordcheck(inputfile_source)