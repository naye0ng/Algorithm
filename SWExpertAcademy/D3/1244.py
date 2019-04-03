"""
1244.최대 상금
"""
import sys
sys.stdin = open('input.txt','r')
from itertools import combinations

def getMax(depth, t) :
    # print(depth, t)
    if depth == N :
        global result
        t= int(''.join(t))
        if result < t :
            result = t
    # 갚은 깊이에 같은 값이 존재하지 않다면
    else :
        for i, j in comb :
            temp = t[:]
            temp[i], temp[j] = temp[j],temp[i]
            if temp not in visited[depth] :
                visited[depth].append(temp)
                getMax(depth+1, temp)

T = int(input())
for test_case in range(1,1+T) :
    number, N = input().split()
    N = int(N)
    number = number.replace('',' ').split()
    comb = list(combinations([i for i in range(len(number))], 2))
    result =0
    visited=[[0] for _ in range(N+1)]
    getMax(0,number)
    print('#{} {}'.format(test_case, result))
