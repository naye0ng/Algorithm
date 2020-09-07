"""
연결리스트(Linked List)
"""
class Node :
    def __init__(self,data,link=None) :
        self.data = data 
        self.link = link

class LinkedList :
    def __init__(self) :
        self.head = None
    
    def addtoFirst(self, data) :
        # head가 가지고 있는 값 자체가 다음 노드이므로 self.head.link가 아니라 self.head가 되어야 한다.
        self.head = Node(data, self.head)

    def add(self, pre, data) :
        if pre == None :
            print("error")
        else :
            pre.link = Node(data,pre.link)
    
    def addtoLast(self, data) :
        if self.head == None :
            self.head = Node(data,None)
        else :
            p = self.head
            # 마지막 노드 찾기
            while p.link != None :
                p = p.link
            
            p.link = Node(data,None)

    # pre의 다음 노드를 삭제
    def delete(self, pre) :
        if pre == None or pre.link == None :
            print('error')
        else :
            pre.link = pre.link.link
    
    def get(self, index) :
        if self.head == None :
            return None
        # 1번째는 head
        p = self.head 

        for _ in range(index-1) :
            # 연결리스트의 크기가 index보다 작은 경우
            if p.link == None :
                return None
            p = p.link
        return p

    def printList(self) :
        if self.head == None :
            print("empty")
        else :
            p = self.head 
            while p.link != None :
                print(p.data, end=' | ')
                p = p.link
            print(p.data)
        


ll = LinkedList()
ll.printList()
ll.addtoLast(1)
ll.addtoLast(2)
ll.addtoLast(3)
ll.addtoFirst(0)
ll.addtoFirst(-1)
ll.printList()

print(ll.get(3).data,"뒤에 삽입")
pre = ll.get(3)
ll.add(pre, 4)
ll.printList()

print(ll.get(4).data,"뒤에 삭제")
pre = ll.get(4)
ll.delete(pre)
ll.printList()