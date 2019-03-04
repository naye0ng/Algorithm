"""
5120.암호
"""
class Node :
    def __init__(self,data,pre=None,next=None) :
        self.data = data
        self.pre = pre
        self.next= next

class DoubleLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def addLast(self,data) :
        if self.head == None :
            self.head = Node(data)
            self.tail = self.head
        else :
            self.tail.next = Node(data,self.tail)
            self.tail = self.tail.next

    def add(self, k, m) :
        p = self.head

        while k :
            for _ in range(m-1) :
                # last node
                if p.next == None :
                    p = self.head
                else : 
                    p = p.next

            if p == self.tail :
                self.tail = Node(p.data+self.head.data,self.tail)
                p.next = self.tail
            else :
                p.next.pre = Node(p.data+p.next.data, p, p.next)
                p.next = p.next.pre
            p = p.next
            
            k -= 1
                
    def printReverse10(self) :
        p = self.tail 
        s = ""
        for _ in range(10):
            s+= str(p.data)+" "

            if p.pre == None :
                break
            p = p.pre
        return s

T = int(input())
for test_case in range(1,T+1) :
    N, M, K = map(int, input().split())

    password = DoubleLinkedList()
    for data in list(map(int, input().split())) :
        password.addLast(data) 

    password.add(K,M)
    
    print(f'#{test_case} {password.printReverse10()}')

