import re


def find_name(line):
    #pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    pattern = r'\w[A-Za-z]+\s\w[A-Za-z]+'
    result = re.findall(pattern, line)
    
    pattern = r'(?:Mr|Mrs|Ms|M|Miss|Madame|Mme|Dr)\.?\s+\w[A-Za-z]+\s+\w[A-Za-z]+'
    result = result + re.findall(pattern,line)

  

    #pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
    #result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)