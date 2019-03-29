class Queue :
    def __init__(self, n) :
        self.n = n
        self.front = -1
        self.rear = -1 
        self.queue = [None]*self.n
    
    def inQueue(self, value) :
        # # 큐가 포화 상태인 경우 출력
        # if self.isFull() :
        #     print("Full")
        self.rear += 1
        self.queue[self.rear] = value

    def deQueue(self) :
        # # 큐가 비어있는 경우 출력
        # if self.isEmpty() :
        #     return None
        self.front += 1
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        return self.rear == self.n-1 
    
    def Qpeek(self) :
        # # 큐가 비어있는 경우 출력
        # if self.isEmpty() :
        #     return None
        return self.queue[self.front+1]


queue = Queue(3)

queue.inQueue(1)
queue.inQueue(2)
queue.inQueue(3)

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
