# gol.py
# Elizabeth Rechtin
# CSCI 77800 Fall 2022
# collaborators: Marieke Thomas and Kiana Herr helped with guidance and debugging 
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

  
  for i in range (r - 1, r + 2):
    if i < 0: #top boundary
      continue
    if i >= len(board1): #bottom boundary
      continue
        
     
    for j in range (c - 1, c + 2):
      if j < 0: #left boundary
        continue
      if j >= len(board1): #right boundary
        continue

      if (r == i and c == j): # checks the square
        continue
      
      if board1[i][j] == 'X':
        #print(i, j)
        livingCt = livingCt + 1
    
  return livingCt

#---------------------------------------------
  #    precond: given a board and a cell
  #    postcond: return next generation cell state based on CGOL rules
  #    (alive 'X', dead ' ')

def getNextGenCell(board1, r, c):
  #checks the neighbors at r and c
  numNeighbours = countNeighbours(board1, r, c)
  dead = '-'
  alive = 'X'
  
  if board1[r][c] == alive:
    if numNeighbours == 2 or numNeighbours == 3:
      nextGen = alive
    else:
        nextGen = dead  
  else:
    if numNeighbours == 3:
      nextGen = alive
    else:
      nextGen = dead

      
  return nextGen
  
#---------------------------------------------
def generateNextBoard(board1):
  newBoard = buildBoard(5, 5)
  for i in range(len(board1)):
    for j in range(len(board1)):
      newBoard[i][j] = getNextGenCell(board1,i,j)
     
  return newBoard
#---------------------------------------------
#test for buildBoard, first with '-', then blank        
#print("This is the empty board: \n")
#print(str(buildBoard(3, 5)))
printBoard(buildBoard(5, 5))
#test for setCell
board1 = buildBoard(5, 5)
# print("This is setCell: \n")
setCell(board1, 0, 0, 'X')
setCell(board1, 0, 1, 'X')
setCell(board1, 1, 0, 'X')
setCell(board1, 3, 2, 'X')
setCell(board1, 3, 3, 'X')
setCell(board1, 3, 4, 'X')
setCell(board1, 4, 0, 'X')
setCell(board1, 4, 3, 'X')
printBoard(board1)
#print(countNeighbours(board1, 2,2))
#newBoard = []
newBoard = generateNextBoard(board1)
printBoard(generateNextBoard(newBoard))

