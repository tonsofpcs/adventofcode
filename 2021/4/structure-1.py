#!/usr/bin/python
import os
import re

print("importing")

inputfile_source = os.path.dirname(__file__) + "/testinput.txt"

def findwinner(boards, numbers):
    for index in range(len(numbers))[4:]:
        testrange = numbers[0:index+1]
        for board in boards:
            continue

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

    for number in callednumbers:
        for index, board in enumerate(markedboards):
            for line in board:
                try: 
                    found = line.index(number)
                    line[found] = "x"
                except: pass


    #    winnerid = findwinner(boards, callednumbers)
    #    result2 = findthing2(line)
    #    result3 = findgroup(line)

    print(markedboards)
    #print(diagonals1, diagonals2)

    #print("Result %s" % result1)
    #print("Result %s" % result2)
    #print("Result %s" % result3)

checkeverything(inputfile_source)