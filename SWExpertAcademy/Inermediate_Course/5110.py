"""

"""
class Node:
    def __init__(self, data, pre=None, link=None):
        self.pre = pre
        self.data = data
        self.link = link


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addtoLast(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.link = Node(data, self.tail)
            self.tail = self.tail.link

    def pushList(self, other):
        p = self.head
        if p.data > other.head.data:
            other.tail.link = p
            p.pre = other.tail
            self.head = other.head
        else:
            while p.link != None:
                if p.link.data > other.head.data:
                    p.link.pre = other.tail
                    other.tail.link = p.link
                    p.link = other.head
                    other.head.pre = p
                    break
                p = p.link
            if p.link == None:
                # p가 마지막 노드 일경우
                p.link = other.head
                other.head.pre = p
                self.tail = other.tail

    def getReverse10(self):
        reverse = []
        p = self.tail
        for _ in range(10):
            # join하기 위해서 str변환
            reverse.append(str(p.data))
            if p.pre == None:
                break
            p = p.pre
        return reverse

    def printAll(self):
        p = self.head
        print(p.data, end=" | ")
        while p.link != None:
            print(p.link.data, end=" | ")
            p = p.link


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    numbers = DoubleLinkedList()
    for k in list(map(int, input().split())):
        numbers.addtoLast(k)

    for _ in range(M - 1):
        target = DoubleLinkedList()
        for k in list(map(int, input().split())):
            target.addtoLast(k)
        numbers.pushList(target)

    print(f'#{test_case} {" ".join(numbers.getReverse10())}')