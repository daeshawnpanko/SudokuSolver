import pprint
from array import *
import numpy as np


def solve(puzzle):
    """
    Changes the 2d array (sudoku puzzle) to the correcr solution
    @param puzzle: A 9x9 2D array of integers, a sudoku puzzle
    @return: True if the puzzle can be solved, False otherwise
    """
    count = 1
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            puzzle[x][y] = count
            count += 1




    for x in range(len(puzzle)):
        print(puzzle[x])
    return True

    # print("This sudoku puzzle cannot be solved")
    # return False


def isValidNumber(puzzle, row, column, number):
    return True


sudoku =   [[1,2,3,4,5,6,7,8,9],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]




print(sudoku)
solve(sudoku)


