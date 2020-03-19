"""
플로이드
https://www.acmicpc.net/problem/11404
플로이드 와샬 참고 : https://m.blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221234427842&proxyReferer=https%3A%2F%2Fwww.google.com%2F
"""

N = int(input())
M = int(input())

"""
[98%에서 에러]
100000을 최대값으로 해줄경우, 500001 + 500001 로 실제 가능한 거리가 나올때 에러 생김
최대 거리값은 100000(입력되는 최대 거리)*100(노드 수) +1
"""

path = [[10000001]*N for _ in range(N)]
for _ in range(M) :
    x, y, c = map(int, input().split())
    path[x-1][y-1] = min(path[x-1][y-1], c)
    
for n in range(N) :
    for x in range(N) :
        if n == x :
            continue
        for y in range(N) :
            if n == y or x == y :
                continue
            # x => y로 가는 최단 경로는 (x,y) 와 (x,n)=>(n,y) 중에 더 작은 값이다.
            path[x][y] = min(path[x][y], path[x][n]+path[n][y])

for x in range(N) :
    for y in range(N) :
        """
        [99%에서 에러]
        못가는 곳은 0을 출력
        """
        if x == y or path[x][y] == 10000001:
            path[x][y] = 0

for i in range(N) :
    print(" ".join(map(str,path[i])))