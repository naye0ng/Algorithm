"""
5108.숫자 추가
"""
class Node :
    def __init__(self,data,link=None) :
        self.data = data
        self.link = link

class LinkedList :
    def __init__(self) :
        self.head = None

    # 리스트에 순차적으로 데이터 삽입하기 위해 생성
    def addtoLast(self, data) :
        if self.head == None :
            self.head = Node(data)
        else :
            p = self.head 
            while p.link != None:
                p = p.link
            # 결과적으로 p는 마지막 노드를 가리키게 됨
            p.link = Node(data)

    # index노드 반환
    def getNode(self, index) :
        p = self.head
        for _ in range(index) :
            p = p.link
        return p

    # index에 값 삽입
    def add(self, index, data) :
        pre = self.getNode(index-1)
        pre.link = Node(data,pre.link)


T = int(input())
for test_case in range(1,T+1) :
    N, M, L = map(int, input().split())

    numbers = LinkedList()
    for n in list(map(int,input().split())) :
        numbers.addtoLast(n)

    for _ in range(M) :
        index, data = map(int, input().split())
        numbers.add(index,data)

    print(f'#{test_case} {numbers.getNode(L).data}')