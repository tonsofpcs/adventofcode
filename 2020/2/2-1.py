#!/usr/bin/python

print "importing"

inputfile_source = "2020/2/input.txt"

def passwordcheck(filename):
    data_min = []
    data_max = []
    data_char = []
    data_pass = []
    data_split = []
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    for item in inputdata:
        dataset = item.split(" ")
        dataset_minmax = dataset[0].split("-")
        data_min.append(dataset_minmax[0])
        data_max.append(dataset_minmax[1])
        data_char.append(dataset[1][:1])
        data_pass.append(dataset[2])
        data_split.append([dataset_minmax[0], dataset_minmax[1], dataset[1][:1],dataset[2]])
    print(inputdata[0:3])
    print(data_split[0:3])
    countgood = 0
    countbad = 0
    count = 0
    for item in data_split:
        allow_min = int(item[0])
        allow_max = int(item[1])
        allow_char = item[2]
        checkpass = item[3]
        allow_count = checkpass.count(allow_char)
        if (allow_max < allow_count) or (allow_min > allow_count):
            countbad += 1
        else:
            countgood += 1
        count += 1

    print("count good: %s", countgood)
    print("count bad: %s", countbad)
    print("count: %s", count)
    print("total: %s", (countgood+countbad))
        
passwordcheck(inputfile_source)