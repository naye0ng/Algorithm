"""
5099.피자 굽기
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
        if self.front == None :
            self.rear = None
        return item[0], item[1]

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
for test_case in range(1, T+1) :
    n, m = map(int, input().split())
    pizza = list(map(int,input().split()))

    queue = LinkedQueue()
    # 화덕에 피자 넣기
    for i in range(n) :
        queue.enQueue([i+1, pizza[i]])
    # pizza = pizza[n:]

    while 1 :
        num, item = queue.deQueue()
        item = item//2

        if queue.isEmpty() :
            print(f'#{test_case} {num}')
            break

        # 피자가 다 구워졌고
        if item == 0 : 
            #구울 피자가 남아있다면
            if n < m :
                n+=1
                queue.enQueue([n,pizza[n-1]])
                # pizza = pizza[1:]
                
        else :
            queue.enQueue([num,item])

