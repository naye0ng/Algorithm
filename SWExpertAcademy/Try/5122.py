"""
5122.수열 편집 
"""
class Node :
    def __init__(self, data, link=None) :
        self.data = data
        self.link = link
    
class LinkedList :
    def __init__(self) :
        self.head = None
    
    def addLast(self,data) :
        if self.head == None :
            self.head = Node(data)
        else :
            p = self.head 
            while p.link != None :
                p = p.link
            p.link = Node(data)
        
    def insert(self, index, data) :
        p = self.head
        for _ in range(int(index)-1) :
            p = p.link
        p.link = Node(data,p.link)
    
    def delete(self, index) :
        p = self.head
        for _ in range(int(index)-1) :
            p = p.link
        p.link = p.link.link
    
    def update(self, index, data) :
        p = self.head
        for _ in range(int(index)) :
            p = p.link
        p.data = data
    
    def printIndexData(self,index) :
        p = self.head
        for _ in range(int(index)) :
            # L 인덱스에 값이 없을 때
            if p.link == None :
                return -1
            p = p.link
        
        return p.data


T = int(input())
for test_case in range(1,1+T) :
    N, M, L = map(int, input().split()) 

    sequence = LinkedList()
    for data in list(map(int, input().split())) :
        sequence.addLast(data)

    for _ in range(M) :
        m = input().split() 
        if m[0] == "I" :
            sequence.insert(m[1],m[2])
        elif m[0] == "D" :
            sequence.delete(m[1])
        else :
            sequence.update(m[1],m[2])

    print(f'#{test_case} {sequence.printIndexData(L)}')
    