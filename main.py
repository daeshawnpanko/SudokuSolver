import pprint
from array import *
import numpy as np
import random as rd


def solve(puzzle):
    """
    Changes the 2d array (sudoku puzzle) to the correcr solution
    @param puzzle: A 9x9 2D array of integers, a sudoku puzzle
    @return: True if the puzzle can be solved, False otherwise
    """
    count = 1
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            puzzle[x][y] = rd.randint(1,9)
            count += 1
        count = 1



    #
    # for x in range(len(puzzle)):
    print(puzzle[x])
    return True

    # print("This sudoku puzzle cannot be solved")
    # return False


def isValidNumber(puzzle, row, column, number):

    #check row
    for x in range(len(puzzle)):
        if puzzle[row][x] == number:
            print("row error",row, ",", x, "is", number)
            return False

    #check column
    for x in range(len(puzzle)):
        if puzzle[x][row] == number:
            print(row,",", x, "is", number)
            return False

    return True


sudoku =   [[0,7,4,0,9,0,0,6,1],
           [9,0,2,1,0,0,3,7,8],
           [0,0,5,0,0,3,0,2,9],
           [4,9,0,0,0,0,0,0,2],
           [2,0,0,9,0,0,7,4,5],
           [7,0,3,0,0,4,0,0,6],
           [6,4,9,0,8,0,0,0,7],
           [5,3,0,7,0,2,9,0,0],
           [8,0,0,0,0,0,0,0,0]]




print(sudoku)
print(isValidNumber(sudoku,0,1,4))
solve(sudoku)


