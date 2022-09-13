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


def setCell(board, r, c, char):
  board[r][c] = char
  return board
  

def printBoard(board):
  for row in board:
    print(row)
  print('\n')
      

def countNeighbours(board1, r, c):
  livingCt = 0

  for row in board1:
    for x in range (r, c):
      if x < 0:
        continue
        if x 
    

  # for row in board1:
  #   if r < 0: #top boundary
  #     continue
  #     if r >= len(board1): #bottom boundary
  #       break

  # for col in board1:
  #   if c < 0: #left boundary
  #     continue
  #     if c >= len(board1[0]): #right boundary
  #       continue
          
  # if r != row & c != col:
  #   if board1[r][c] == 'X':
  #     livingCt = livingCt + 1

  return livingCt
  



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


  #rows = '-'
  
  
   

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
