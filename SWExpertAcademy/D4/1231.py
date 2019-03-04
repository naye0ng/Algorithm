"""
1231.중회순회
"""
import sys
sys.stdin = open("input.txt", "r")

def inorder(T) :
    global result
    if T :
        inorder(tree[T][1])
        result += tree[T][0]
        inorder(tree[T][2])



for test_case in range(1,11) :
    N = int(input())

    tree = [[0]*3 for _ in range(N+1)]

    for _ in range(N) :
        m = input().split()

        node = tree[int(m[0])]
        node[0] = m[1]
        if len(m) == 3 :
            node[1] = int(m[2])
        elif len(m) == 4 :
            node[1] = int(m[2])
            node[2] = int(m[3])

    result = ""
    inorder(1)
    print("#{} {}".format(test_case, result))