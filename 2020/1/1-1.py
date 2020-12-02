#!/usr/bin/python

print "importing"

inputfile_source = "2020/1/input.txt"

def find2020(filename):
    inputfile = open(filename)
    inputdata = inputfile.readlines()
    inputdata2 = inputdata
    for line1 in inputdata:
        for line2 in inputdata2:
            if (int(line1) + int(line2) == 2020):
                print(line1)
                print(line2)
                print(str(int(line1)*int(line2)))
                return

print("1")
print(find2020(inputfile_source))
print("2")