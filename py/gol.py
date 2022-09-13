# gol.py
# Elizabeth Rechtin
# CSCI 77800 Fall 2022
# collaborators: Marieke Thomas met with me over the weekend when I was stuck and she helped me sort out some of my errors. 
# consulted: my gol.java from the programming class, Thinkcspy from runestone academy, Python Documentation site at docs.python.org,   



def buildBoard(rows, cols):
  
  board = [] #develop empty board/list
  char = '-' #fill with '-' just so I can see if it worked

  for i in range(rows):
    board.append([])
    for j in range(cols):
      board[i].append(char)
      
  return board


#---------------------------------------------
def setCell(board, r, c, char):
  board[r][c] = char
  return board
  

#---------------------------------------------
def printBoard(board):
  for row in board:
    print(row)
  print('\n')
      

#----------------------------------------------
def countNeighbours(board1, r, c):
  livingCt = 0

  
  for i in range (r -1, r + 2):
    if i - 1 < 0: #top boundary
      continue
    if i + 1 > len(board1): #bottom boundary
      continue
        
     
    for j in range (c - 1, c + 2):
      if j - 1 < 0: #left boundary
        continue
      if j + 1 > len(board): #right boundary
        continue

      if (r == i and c == j): # checks the square
        continue
      
      if board1[i][j] == 'X':
        print(i, j)
        livingCt = livingCt + 1
    
  return livingCt

#---------------------------------------------
  # for row in board1:
  #   if r - 1 < 0: #top boundary
  #     
  #     if r + 1 >= len(board1): #bottom boundary
  #       break

  # for col in board1:
  #   if c - 1 < 0: #left boundary
  #     continue
  #     if c + 1 >= len(board1[0]): #right boundary
  #       continue
          
  # if r != row and c != col:
  #   if board1[r][c] == 'X':
  #     livingCt = livingCt + 1
#---------------------------------------------



#test for buildBoard, first with '-', then blank        
#print("This is the empty board: \n")
#print(str(buildBoard(3, 5)))
printBoard(buildBoard(3, 5))
#test for setCell
board1 = buildBoard(5, 5)
# print("This is setCell: \n")
setCell(board1, 0, 0, 'X')
setCell(board1, 0, 1, 'X')
setCell(board1, 1, 0, 'X')
setCell(board1, 3, 2, 'X');
setCell(board1, 3, 3, 'X');
setCell(board1, 3, 4, 'X');
setCell(board1, 4, 0, 'X');
setCell(board1, 4, 3, 'X');

printBoard(board1)
print(countNeighbours(board1, 0,0))


 
  
  
   

#def applyRules(ch):
#  newCh = ""
 # if ch == "X":


    

#firstRow = (chr(89)*3)
#secondRow = ("X" + "X" + "X")
#thirdRow = ("X" + "X" + "X")
# print(ord("X"))

#if firstRow == "XXX":
  #print("yes")
#else: 
  #print("no")

#print(firstRow)
#print(secondRow)
#print(thirdRow)

#print(chr(2777))

#print(buildBoard(3, 3))
