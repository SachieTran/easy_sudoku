filename = input("Please enter the text file's name: ")
infile = open(filename, "r")




for line in infile :
   line = line.strip()
   puzzleList = line.split()
   row = int(puzzleList[0])
   col = int(puzzleList[1])
   value = int(puzzleList[2])
   print(puzzleList)
   