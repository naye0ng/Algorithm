"""
5105.미로의 거리
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

dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())
for test_case in range(1, 1+T) :
    n = int(input())
    mirro = [ list(map(int, input().replace(""," ").split())) for _ in range(n)]

    # 시작점 찾기
    startX, startY = -1, -1
    for x in range(n) :
        for y in range(n) :
            if mirro[x][y] == 2 :
                startX = x
                startY = y
                break
    
    queue = LinkedQueue() 
    queue.enQueue([0,startX,startY])

    result = 0
    breakPT = True
    while breakPT :
        # 큐에 아무것도 없는 경우
        if queue.isEmpty() :
            break
        item = queue.deQueue()
        m = item[0]
        x = item[1]
        y = item[2]

        # 통로찾기
        for i in range(4):
            if x+dx[i] < n and x+dx[i] >= 0 and y+dy[i] < n and y+dy[i] >= 0 :
                if mirro[x+dx[i]][y+dy[i]] == 0 :
                    queue.enQueue([m+1,x+dx[i],y+dy[i]]) 
                    mirro[x+dx[i]][y+dy[i]] = 1
                    continue

                if mirro[x+dx[i]][y+dy[i]] == 3 :
                    result = m
                    breakPT = False
                    break

    print(f'#{test_case} {result}')







    
