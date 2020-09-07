"""
클래스로 구현
"""

class Node :
    def __init__(self, item, n=None) :
        self.item = item
        self.next = n

class LinkedQueue :
    def __init__(self) :
        # front랑 rear모두 Node가 될것임
        self.front = None
        self.rear = None

    def enQueue(self, item) :
        # 새로운 노드 생성
        newNode = Node(item)
        # 처음으로 생성된 노드이면 front는 새로 생성된 노드를 가리킴
        if self.front == None :
            self.front = newNode
        else :
            # 현재의 마지막 노드에 다음 노드 할당
            self.rear.next = newNode
        # 마지막 노드 가리키도록 rear값 변경
        self.rear = newNode

    def deQueue(self) :
        if self.isEmpty() :
            return None
        
        item = self.front.item
        self.front = self.front.next

        # 그런데 만약 마지막 노드라면 마지막 노드를 가리키는 rear 변경
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

queue = LinkedQueue()
queue.enQueue(5)
queue.enQueue(6)
print(queue.printQ())

print(queue.deQueue())
print(queue.deQueue())
print(queue.printQ())



"""
함수로 구현
"""

# def enQueue(item) :
#     global front, rear
#     # 새로운 노드 생성
#     newNode = Node(item)
#     # 큐가 비어 있다면
#     if front == None :
#         # front에는 노드가 있음을 연결
#         front = newNode
#     else :
#         rear.next = newNode
#     rear = newNode

# def isEmpty() :
#     return front == None


# def deQueue() :
#     global front, rear
#     if isEmpty() :
#         return None

#     item = front.item
#     front = front.next

#     if front == None :
#         rear = None 
#     return item


# def Qpeek() :
#     return front.item

# def printQ() :
#     f = front
#     s = ""
#     while f :
#         s += str(f.item)+" "
#         f = f.next
#     return s

# front, rear = None, None
# enQueue(5)
# enQueue(6)
# deQueue()
# print(printQ())