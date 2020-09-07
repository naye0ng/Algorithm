"""
이진검색 
"""

def binarySearch(x) :
    searchList = [i for i in range(1,11)] 
    
    pl = 0
    pr = len(searchList)-1
    
    while 1 :
        pm = (pl+pr)//2
        if x == searchList[pm]:
            return pm
        elif x < searchList[pm]:
            pr = pm
        else :
            pl = pm

print(binarySearch(8))