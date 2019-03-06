"""
5178.노드의 합
"""
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T+1) :
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]

    for _ in range(M):
        index, value  = map(int, input().split())
        tree[index] = value

    # 마지막 노드가 짝수라면
    if N%2 == 0 :
        tree[N//2] = tree[N]
        N -= 1

    for i in range(N,1,-2) :
        tree[i//2] = tree[i]+tree[i-1]

    print('#{} {}'.format(test_case,tree[L]))




