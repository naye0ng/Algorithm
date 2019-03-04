"""
5174.subtree
"""
import sys
sys.stdin = open('input.txt','r')

def preorder(t) :
    if t :
        global result
        result +=1
        preorder(tree[t][0])
        preorder(tree[t][1])

T = int(input())
for test_case in range(1, 1+T) :
    E, N = map(int, input().split())
    m = list(map(int, input().split()))

    tree = [ [0]*2 for _ in range(E+2) ]

    for i in range(0,len(m),2) :
        if tree[m[i]][0] == 0:
            tree[m[i]][0] = m[i+1]
        else :
            tree[m[i]][1] = m[i + 1]

    result = 0
    preorder(N)
    print('#{} {}'.format(test_case, result))