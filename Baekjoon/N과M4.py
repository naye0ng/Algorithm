"""
N과 M (4)
https://www.acmicpc.net/problem/15652
"""

# 중복조합
def getPerm(N,M,depth,k,nums) :
    if depth == M :
        print(" ".join(nums))
    else :
        for i in range(k,N) :
            getPerm(N,M,depth+1,i, nums+[numbers[i]])

N, M = map(int,input().split())
numbers = [str(n) for n in range(1,N+1)]
getPerm(N,M,0,0,[])