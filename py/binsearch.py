# binsearch.py
# Elizabeth Rechtin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: Kiana Herr, my SortSearch.java from the programming class, Thinkcspy from runestone academy, Python Documentation site at docs.python.org,



def binarySearch(mylist, x):
  low = 0
  high = len(mylist) -1
  middle = int((low + high) /2) 
 
  
  while True:
    if x == mylist[int(middle)]: 
      return middle

    elif x < mylist[int(middle)]: 
      high = middle - 1
      middle = int((low + high) /2)

    elif high <= low:
      return - 1

    else:
      low = middle + 1
      middle = int((low + high) /2) 
    


mylist = [2, 5, 10, 22, 30, 33, 62, 65, 78, 82, 97]
print(binarySearch(mylist, 33))


