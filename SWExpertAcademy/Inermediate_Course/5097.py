"""
5097.회전
"""
class Node :
    def __init__(self, item, n = None) :
        self.item = item
        self.next = n
    
class LinkedQueue :
    def __init__(self) :
        self.front = None
        self.rear = None
    
    def enQueue(self, item) :
        newNode = Node(item)

        if self.front == None :
            self.front = newNode
        else :
            self.rear.next = newNode
        self.rear = newNode

    def deQueue(self) :
        if self.isEmpty() :
            return None
        item = self.front.item
        self.front = self.front.next
        # 마지막 1개의 노드 처리
        if self.front == None :
            self.rear = None
        return item

    def isEmpty(self) :
        return self.front == None
    
    def Qpeek(self) :
        return self.front.item

    def printQ(self) :
        f = self.front
        s = ""
        while f :
            s += str(f.item)+" "
            f = f.next
        return s


T = int(input())
for test_case in range(1,T+1):
    n, m = map(int, input().split())
    inputData = list(map(int, input().split()))

    queue = LinkedQueue() 
    for data in inputData :
        queue.enQueue(data)

    for _ in range(m) :
        item = queue.deQueue()
        queue.enQueue(item)
    
    print(f'#{test_case} {queue.Qpeek()}')