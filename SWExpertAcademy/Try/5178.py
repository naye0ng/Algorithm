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

    # for i in range(N,0,-1) :
    #     # 마지막 노드이면서 짝수이면
    #     if i == N and i//2 == 0 :
    #




