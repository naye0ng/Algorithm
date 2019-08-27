"""
N과 M (5)
https://www.acmicpc.net/problem/15654
"""

def perm(N, M, depth, result) :
    if M == depth :
        print(" ".join(result))
    else :
        for i in range(N) :
            if visited[i] == False :
                visited[i] = True
                perm(N,M,depth+1, result+[str(numbers[i])])
                visited[i] = False

N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
visited = [False]*N
perm(N, M, 0, [])
