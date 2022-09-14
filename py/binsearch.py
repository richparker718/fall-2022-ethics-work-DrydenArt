# binsearch.py
# Elizabeth Rechtin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: my SortSearch.java from the programming class, Thinkcspy from runestone academy, Python Documentation site at docs.python.org



def binarySearch(mylist, x):
  low = 0
  high = len(mylist) -1
  middle = (high + low) /2
 
  
  while True:
    if middle == x:
      return middle

    elif x < middle:
      high = middle - 1

    elif high <= low:
      return - 1

    else:
      low = middle + 1
      middle = (low + high) /2
    
  #return result


mylist = [2, 5, 10, 22, 30, 33, 62, 65, 78, 82]
#x = 33
#result = binarySearch(mylist, x)
print(binarySearch(mylist, 33))


