"""
N과 M (7)
https://www.acmicpc.net/problem/15656
"""
#  중복순열
def perm(N, M, depth, result) :
    if M == depth :
        print(" ".join(result))
    else :
        for i in range(N) :
            perm(N,M,depth+1, result+[str(numbers[i])])

N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
perm(N, M, 0, [])

