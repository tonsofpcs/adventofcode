#!/usr/bin/python
import os
import re

print("importing")

inputfile_source = os.path.dirname(__file__) + "/input.txt"

def findlastwinner(boards, numbers):

    diagonals1 = []
    diagonals2 = []
    for board in boards:
        diagonals1.append(
            [
                board[0][0],
                board[1][1],
                board[2][2],
                board[3][3],
                board[4][4]
            ])
        diagonals2.append(
            [
                board[0][4],
                board[1][3],
                board[2][2],
                board[3][1],
                board[4][0]
            ])

    markedboards = list(boards)
    doneline = ['x','x','x','x','x']

    haswon = []
    allwon = []

    for index in range(len(markedboards)):
        haswon.append(False)
        allwon.append(True)

    for number in numbers:
        for index, board in enumerate(markedboards):
            for line in board:
                try: 
                    found = line.index(number)
                    line[found] = "x"
                    if line == doneline:
                        print("Found one! %s" % index)
                        haswon[index] = True
                        if haswon == allwon:
                            return(index, number,board)
                except: pass
            for line in list(map(list, zip(*board))):
                if line == doneline:
                    print("Found one! map %s" % index)
                    haswon[index] = True
                    if haswon == allwon:
                        return(index, number,board)
            

def findthing2(testrange):
    seekvalue = 0
    for item in testrange:
        seekvalue = 1
    return seekvalue

def findgroup(testgroup):
    return (findthing1(testgroup[1]) + findthing2(testgroup[2]))

def checkeverything(filename):
    inputfile = open(filename)
    inputfiledata = inputfile.read()
    inputdata = inputfiledata.split("\n")

    callednumbers = inputdata[0].split(",")

    boards = []

    print(callednumbers)
    for index in range(int((len(inputdata)-1)/6)):
        board = []
        for line in inputdata[index*6+2:index*6+7]:
            board.append(re.split(" +",line.strip(" ")))
        boards.append(board)


    winnerid, lastnum, winningboard = findlastwinner(boards,callednumbers)
    print(winnerid, lastnum, winningboard)

    sumboard = 0
    for line in winningboard:
        for item in line:
            if not(item == 'x'):
                sumboard += int(item)
    result1 = sumboard * int(lastnum)

    #    winnerid = findwinner(boards, callednumbers)
    #    result2 = findthing2(line)
    #    result3 = findgroup(line)

    #print(markedboards)
    #print(diagonals1, diagonals2)

    print("Result %s" % result1)
    #print("Result %s" % result2)
    #print("Result %s" % result3)

checkeverything(inputfile_source)