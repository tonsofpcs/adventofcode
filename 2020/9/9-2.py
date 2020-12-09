#!/usr/bin/python
import os

print "importing"

inputfile_source = os.path.dirname(__file__) + "/input.txt"
testlength = 25

def testpair(testrange, sumtocheck):
    success = 0
    for item in testrange:
        for item2 in testrange:
            if (item + item2) == sumtocheck:
                success = 1
                break
    return success

def checkeverything(filename):
    inputfile = open(filename)
    rawinputdata = inputfile.readlines()
    inputdata = []
    for item in rawinputdata:
        inputdata.append(int(item))

    for index, line in enumerate(inputdata):
        if index >= testlength:
            success = testpair(inputdata[index-(testlength):index],line)
            if not(success): break
    
    return findsumrange(inputdata, line)

def findsumrange(dataset,sumtofind):
    length = len(dataset)
    startpos = 0
    index = 2
    result = 0
    while startpos < (length-2):
        cursum = sum(dataset[startpos:index])
        print(dataset[startpos:index], cursum, sumtofind)
        if cursum == sumtofind:
            result = dataset[startpos:index]
            return [result, min(result)+max(result)]
        elif (cursum > sumtofind) or (index == length):
            startpos += 1
            index = startpos + 2
        else:
            index += 1
    
    if result:
        return [result, min(result)+max(result)]
    return ("Error")


print(checkeverything(inputfile_source))