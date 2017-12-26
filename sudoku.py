# sudoku.py
#
# Created by: Tran Tran
# Date : 05/01/2016
#
#
# The program implements a driver module that solves a Sudoku puzzle using 
# a recursive backtracking algorithm.

from sudokugrid import SudokuGrid

def main() :
   # Prompt the user for the text file's name.
   filename = input("Please enter the text file's name: ")
   
   # Create and configure the grid.
   mySudoku = SudokuGrid()
   
   # Load the file.
   mySudoku.load(filename)
   
   # Solve the problem and print the solution.
   solveSudoku(mySudoku)
   mySudoku.print()

# Recursion funtion to solve the puzzle.
def solveSudoku(mySudoku) :
   myTuple = mySudoku.findOpenCell() 
   if myTuple is None :
      return True
   else :
      row = myTuple[0]
      col = myTuple[1]
      for i in range(1, 10) :
         if mySudoku.isValid(row, col, i) :
            mySudoku.setCell(row, col, i)
            
            # Using recursion to solve the next problem.
            solution = solveSudoku(mySudoku)
            if solution :
               return True
            mySudoku.setCell(row, col, 0)
            
      # Backtracking.      
      return False      

# Start the program.   
main()
