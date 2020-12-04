#!/usr/bin/python

print "importing"

inputfile_source = "2020/4/input.txt"

def checkid(idstring):
    items = idstring.split(" ")
    if (len(items) < 7): return 0
    validitem = 0
    for item in items:
        caseselect = {
            "byr": 1,
            "iyr": 1,
            "eyr": 1,
            "hgt": 1,
            "hcl": 1,
            "ecl": 1,
            "pid": 1,
            "cid": 0
        }
        validitem += caseselect.get(item[0:3], 0)
    return (validitem >= 7)


def checkfile(filename):
    validids = 0

    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n\n")
    for line in inputdata:
        line = line.replace("\n"," ")
        print(line)
        if len(line) == 0:
            continue
        validids += checkid(line)
    return validids

print(checkfile(inputfile_source))