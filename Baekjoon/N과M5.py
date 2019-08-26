"""
N과 M (5)
https://www.acmicpc.net/problem/15654
"""

def getPerm(N, M, visited, depth, before) :
    if depth == M :
        print(" ".join(before))
    else :
        for i in range(N) :
            if visited[i] == False :
                visited[i] = True
                getPerm(N, M, visited, depth+1, before + [number[i]])
                visited[i] = False

N, M = map(int, input().split())
number = input().split()
number.sort()
visited = [False]*N
# perm = dict()
#  이경우 문제 생김
getPerm(N, M, visited, 0, [])

"""
4 3
1 1 1 1
"""