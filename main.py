import pprint
from array import *
import numpy as np
import time



def solve(puzzle):
    """
    Changes the 2d array (sudoku puzzle) to the correcr solution
    @param puzzle: A 9x9 2D array of integers, a sudoku puzzle
    @return: True if the puzzle can be solved, False otherwise
    """

    # check if there are still empty boxes
    empty = findEmpty(puzzle)
    if not empty:
        return True
    else:
        row = empty[0]  # x
        col = empty[1]  # y

    for x in range(1, 10):
        if isValidNumber(puzzle, row, col, x):
            puzzle[row][col] = x

            if solve(puzzle):
                return True
            # reset to 0 if not valid
            puzzle[row][col] = 0
    return False


def isValidNumber(puzzle, row, column, number):
    """
    checks if there is a conflicting number in the row or column
    @param puzzle: the sudoku that you are checking
    @param row: the row in which you want to check for conflicts
    @param column: the column in which you want to check for conflicts
    @param number: the number you are trying to check validation
    @return: True if the number currently fits, False if it does not fit
    """

    # Check for the same number in the current row
    for x in range(len(puzzle)):
        if puzzle[row][x] == number:
            #print("row error: ",row, ",", x, "already has a", number)
            return False

    # Checks for the current number in the current column
    for x in range(len(puzzle)):
        if puzzle[x][column] == number:
            #print("column error: ", x,",", column, "already has a ", number)
            return False

    pos = [row, column]
    # check for the current number in the current 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == number and (i, j) != pos:
                return False

    return True


def findEmpty(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            if puzzle[x][y] == 0:
                return (x,y)
    return



sudoku =   [[0,0,0,6,0,0,0,3,8],
           [1,8,6,0,3,7,0,4,2],
           [7,0,4,8,5,2,0,9,1],
           [0,0,0,0,7,9,0,0,4],
           [6,7,0,4,0,5,0,0,0],
           [0,0,9,0,0,0,8,0,0],
           [3,0,7,0,0,0,2,0,6],
           [0,0,0,5,0,0,0,0,7],
           [8,9,0,0,2,0,4,0,0]]


def printPuzzle(puzzle):
    for x in range(len(puzzle)):
        print(puzzle[x])


def main():
    print('Unsolved:')
    printPuzzle(sudoku)
    solve(sudoku)
    print('Solved:')
    printPuzzle(sudoku)


if __name__ == '__main__':
    main()
