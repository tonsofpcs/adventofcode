#!/usr/bin/python

print "importing"

inputfile_source = "2020/4/valid.txt"

def checkid(idstring):
    hexvalid = "0123456789abcdef"
    numvalid = "0123456789"
    eyecolors = {"amb":1,"blu":1,"brn":1,"gry":1,"grn":1,"hzl":1,"oth":1}
    items = idstring.split(" ")
    if (len(items) < 7): return 0
    validitem = 0
    for item in items:
        checkcase = item[0:3]
        checkvalue = item[4:]
        if checkcase == "byr":
            if (len(checkvalue) == 4 and (int(checkvalue) >= 1920) and (int(checkvalue) <= 2002)):
                print("byr valid")
                validitem += 1
        elif checkcase == "iyr":
            if (len(checkvalue) == 4 and (int(checkvalue) >= 2010) and (int(checkvalue) <= 2020)):
                print("iyr valid")
                validitem += 1
        elif checkcase == "eyr":
            print("eyr valid")
            if (len(checkvalue) == 4 and (int(checkvalue) >= 2020) and (int(checkvalue) <= 2030)):
                validitem += 1
        elif checkcase == "hgt":
            if checkvalue[-2:] == "cm":
                if (len(checkvalue) == 5 and (int(checkvalue[0:3]) >= 150) and (int(checkvalue[0:3]) <= 193)):
                    print("hgt valid")
                    validitem += 1
            elif checkvalue[-2:] == "in":
                if (len(checkvalue) == 4 and (int(checkvalue[0:2]) >= 59) and (int(checkvalue[0:2]) <= 76)):
                    print("hgt valid")
                    validitem += 1
        elif checkcase == "hcl":
            if checkvalue[0:1] == "#":
                if (len(checkvalue[1:]) == 6 and all(c in hexvalid for c in checkvalue[1:])):
                    print("hcl valid")
                    validitem += 1
        elif checkcase == "ecl":
            print("ecl valid")
            validitem += eyecolors.get(checkvalue, 0)
        elif checkcase == "pid":
            if (len(checkvalue) == 9 and all(c in numvalid for c in checkvalue)):
                print("pid valid")
                validitem += 1
    print((validitem >= 7))
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