#!/usr/bin/python
import os
import copy

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

maxdays = 8
spawndays = 8
resetdays = 6
daystorun = 80

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    print(inputfiledata)
    lanternfish = list(map(int, inputfiledata.split(",")))

    fishsim = []
    blankfishsim = []
    for day in range(maxdays+1):
        blankfishsim.append(0)
        fishsim.append(lanternfish.count(day))
        print(fishsim[day])

    for day in range(daystorun):
        newfishsim = list(blankfishsim) #copy the blank list
        for daysleft in range(maxdays+1):
            if daysleft == 0:
                newfishsim[resetdays] += fishsim[0]
                newfishsim[spawndays] += fishsim[0]
            else:
                newfishsim[daysleft-1] += fishsim[daysleft]
        fishsim = list(newfishsim) #copy the new list over
    
    return(sum(fishsim))

            
print(checkeverything(inputfile_source))