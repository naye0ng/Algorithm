"""
5877.이진 힙
"""
import sys
sys.stdin = open('input.txt','r')

def changeData(index) :
    if index > 1 and tree[index] < tree[index // 2]:
        temp = tree[index]
        tree[index] = tree[index//2]
        tree[index//2] = temp
        return changeData(index//2)

def sumPre(index) :
    if index == 1 :
        return 0
    return tree[index//2] + sumPre(index//2)

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    tree = [ 0 for _ in range(N+1)]

    index = 1
    for t in map(int, input().split()) :
        tree[index] = t
        changeData(index)
        index+=1

    print("#{} {}".format(test_case, sumPre(N)))

