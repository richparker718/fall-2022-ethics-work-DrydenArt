# nim.py
# Elizabeth Rechtin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: my Nim.java from the programming class, Thinkcspy from runestone academy and W3Schools.org

import random

stones = 12
print("There are", stones, "stones")
#returns a number between 1 (included) and 4 (not included)
computer_stones_taken = random.randrange(1, 4)

# print("no loop")


while stones > 0:
  user_stones_taken = (int(input("Please enter a number from 1 - 3 stones: ")))
  stones = (stones - user_stones_taken)
  print("There are", stones, "remaining")
  
  if stones <= 0:
    print("You win!")
    break
     
  print("The computer chooses", computer_stones_taken)
  stones = (stones - computer_stones_taken)
  if stones <= 0:
    print("The computer wins!")
    break
    
  print("There are", stones, "remaining")
  
  


