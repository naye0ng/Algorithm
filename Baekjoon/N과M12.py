"""
N과 M (12)
https://www.acmicpc.net/problem/15664
"""

def perm(N, M, depth,k, result) :
    if M == depth :
        res.append(result)
    else :
        for i in range(k, N) :
            perm(N,M,depth+1,i, result+[numbers[i]])


N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
res = []
perm(N, M, 0, 0,[])
res = sorted(list(set(map(tuple,res))))
for r in res :
    print(" ".join(map(str,r)))