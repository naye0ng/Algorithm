"""
N과 M (10)
https://www.acmicpc.net/problem/15664
"""

def perm(N, M, depth, k, result) :
    if M == depth :
        res.append(result)
    else :
        for i in range(k,N) :
            if visited[i] == False :
                visited[i]= True
                perm(N,M,depth+1, i+1, result+[numbers[i]])
                visited[i] =False

N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
visited = [False]*N
res = []
perm(N, M, 0, 0,[])
res = sorted(list(set(map(tuple,res))))
for r in res :
    print(" ".join(map(str,r)))

