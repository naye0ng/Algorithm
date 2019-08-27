"""
N과 M (1)
https://www.acmicpc.net/problem/15649
"""

def getPerm(N,M,depth,nums) :
    if depth == M :
        print(" ".join(nums))
    else :
        for i in range(N) :
            if visited[i] == False :
                visited[i] = True
                getPerm(N,M,depth+1, nums+[numbers[i]])
                visited[i] = False    

N, M = map(int,input().split())
numbers = [str(n) for n in range(1,N+1)]
visited = [False]*N
getPerm(N,M,0,[])
