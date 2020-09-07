class RoundQueue :
    def __init__(self, n) :
        self.n = n
        self.front = 0
        self.rear = 0 
        self.queue = [None]*self.n
    
    def inQueue(self, value) :
        # 큐가 포화 상태인 경우 출력
        if self.isFull() :
            print("Full")
        self.rear = (self.rear+1)%self.n
        self.queue[self.rear] = value

    def deQueue(self) :
        # # 큐가 비어있는 경우 출력
        # if self.isEmpty() :
        #     return None
        self.front = (self.front+1)%self.n
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        # 원형 큐의 경우 원형을 돌아왔는데 값이 front랑 같다면 full이라고 볼 수 있다.
        return (self.rear+1)%self.n == self.front
    
    def Qpeek(self) :
        # # 큐가 비어있는 경우 출력
        # if self.isEmpty() :
        #     return None
        return self.queue[self.front+1]


queue = RoundQueue(5)

queue.inQueue(1)
queue.inQueue(2)
queue.inQueue(3)
queue.inQueue(4)
queue.inQueue(5)
print(queue.queue)

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.queue)