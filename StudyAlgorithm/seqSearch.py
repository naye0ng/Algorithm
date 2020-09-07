"""
선형 검색 

"""

def seqSearch(x) :
    searchList = [1,10,2,9,7,3,4,6,5,8]
    # x가 searchList에 없을 경우 : 보초법 
    searchList.append(x)

    for i in range(len(searchList)) :
        if searchList[i] == x :
            return i if i != len(searchList)-1 else -1


print(seqSearch(8))