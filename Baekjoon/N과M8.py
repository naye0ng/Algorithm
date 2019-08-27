"""
N과 M (8)
https://www.acmicpc.net/problem/15657
"""

def comb(N, M, depth, k, result) :
    if M == depth :
        print(" ".join(result))
    else :
        for i in range(k,N) :
            comb(N,M,depth+1,i, result+[str(numbers[i])])

N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
comb(N, M, 0,0,[])
