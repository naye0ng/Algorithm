"""
N과 M (3)
https://www.acmicpc.net/problem/15651
"""
# 중복순열
def getPerm(N,M,depth,nums) :
    if depth == M :
        print(" ".join(nums))
    else :
        for i in range(N) :
            getPerm(N,M,depth+1, nums+[numbers[i]])

N, M = map(int,input().split())
numbers = [str(n) for n in range(1,N+1)]
getPerm(N,M,0,[])