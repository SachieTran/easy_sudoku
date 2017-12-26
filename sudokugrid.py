# sudokugrid.py
#
# Created by: Tran Tran
#
#
# The program implements  the SudokuGrid ADT that will be used to represent 
# the puzzle grid.

from ezarrays import Array2D

# Values representing the empty cell on the grid.
EMPTY = 0
   
class SudokuGrid():
   
   # Creates a new Sudoku grid of empty cells.
   def __init__(self) :
      self._grid = Array2D(9, 9)
      self._grid.clear(EMPTY)
      
   # Clears the grid and loads an initial Sudoku puzzle configuration from a
   # text file, the name of which is provided as an argument.
   def load(self, filename):
      infile = open(filename, "r")
      for line in infile :      
         line = line.strip()
         puzzleList = line.split()
         row = int(puzzleList[0])
         col = int(puzzleList[1])
         value = int(puzzleList[2])
         self._grid[row, col] = value
      infile.close()
      
   # Sets the indicated cell to the given digit. The row and col indices 
   # must be within the valid range.
   def setCell(self, row, col, digit):
      assert row >= 0 and col >= 0 and row < 9 and col < 9, \
             "Invalid cell position."
      self._grid[row, col] = digit
   
   # Clears the indicated cell. The row and col indices must be within the 
   # valid range.
   def clearCell(self, row, col):
      assert row >= 0 and col >= 0 and row < 9 and col < 9, \
             "Invalid cell position."      
      self._grid[row, col] = EMPTY
   
   # Returns a Boolean that indicates if the given cell is empty. The row
   # and col indices must be within the valid range.
   def isEmpty(self, row, col):
      assert row >= 0 and col >= 0 and row < 9 and col < 9, \
             "Invalid cell position."     
      if self._grid[row, col] == EMPTY :
         return True
      else :
         return False
   
   # Returns a Boolean that indicates if placing the given digit in
   # the given cell is a valid move.
   def isValid(self, row, col, digit):
      assert row >= 0 and col >= 0 and row < 9 and col < 9, \
             "Invalid cell position."  
      assert digit > 0 and digit <= 9, "Invalid digit."
      
      # Check each row and column.
      for i in range(9) :
         if self._grid[row, i] == digit :
            return False
      for j in range(9) :
         if self._grid[j, col] == digit :
            return False
      
      # Check each subsquare by finding its top left value.
      topRow = (row // 3) * 3
      topCol = (col // 3) * 3
      for i in range(topRow, topRow + 3) :
         for j in range(topCol, topCol + 3) :
            if self._grid[i, j] == digit :
               return False
      return True
         
   
   # Searches the grid for an open cell.
   def findOpenCell(self):
      for i in range(9) :
         for j in range(9) :
            if self.isEmpty(i, j) :
               return (i, j)
      return None

   # Prints the grid to the terminal in the following format.
   def print(self) :
      print("", "-" * 23, "")
      for i in range(3) :
         print("|", end=" ")
         for j in range(9) :
            if j == 3 or j == 6 :
               print("|", end=" ")
               print("%d" % self._grid[i, j], end=" ")
            else :
               print("%d" % self._grid[i, j], end=" ")
         print("|")
         
      print("", "-" * 23, "")
      for i in range(3, 6) :
         print("|", end=" ")
         for j in range(9) :
            if j == 3 or j == 6 :
               print("|", end=" ")
               print("%d" % self._grid[i, j], end=" ")
            else :            
               print("%d" %self._grid[i, j], end=" ")  
         print("|")
         
      print("", "-" * 23, "")
      for i in range(6, 9) :
         print("|", end=" ")
         for j in range(9) :
            if j == 3 or j == 6 :
               print("|", end=" ")
               print("%d" % self._grid[i, j], end=" ")
            else :            
               print("%d" %self._grid[i, j], end=" ") 
         print("|")
      print("", "-" * 23, "")
      
            
