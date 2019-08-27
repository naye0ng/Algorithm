"""
N과 M (11)
https://www.acmicpc.net/problem/15664
"""
def perm(N, M, depth, result) :
    if M == depth :
        res.append(result)
    else :
        for i in range(N) :
            perm(N,M,depth+1, result+[numbers[i]])


N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
res = []
perm(N, M, 0,[])
res = sorted(list(set(map(tuple,res))))
for r in res :
    print(" ".join(map(str,r)))
