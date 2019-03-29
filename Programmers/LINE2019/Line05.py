"""
백준 17071 찾아보기
"""



def BFS(t, c, b) :
    print(t,"코니",c,"브라운",b, visited[b])
    if t == 6 :
        return 200000
    if len(visited[b]) == 0 or c > 200000:
        return 2000
    # 방문한 적 없을 때만
    else :
        for v in visited[b] :
            if c == v :
                # print("같당ㅇ당")
                return t
        global C
        nextC = C+t*(t+1)//2

        b1, b2, b3 = visited[b][0], visited[b][1], visited[b][2]
        # visited 체크하기
        visited[b] = []
        bfs1, bfs2, bfs3 = 2000, 2000, 2000

        if b1 > 0 and b1 < 200000 :
            bfs1 = BFS(t+1, nextC, b1)
        if b2 > 0 and b2 < 200000 :
            bfs2 = BFS(t+1, nextC, b2)
        if b3 > 0 and b3 < 200000 :
            bfs3 = BFS(t+1, nextC, b3)
        # print(b1, b2, b3)
        visited[b] = [b1, b2, b3]
        return min(bfs1, bfs2, bfs3)


C, B = map(int, input().split())
t = 0
visited = [[i-1,i+1,i*2] for i in range(200001)]
nextC = C+t*(t+1)//2
print(BFS(t+1,nextC,B))
    


    # if ===
    # if b == c :
    #     return t
    # nextC = c+t*(t+1)//2
    # if nextC > 200000 :
    #     return 0
    # else :
    #     # 이전에 + 했다면 -를 하면 당근 안돼!
    #     b1, b2, b3 = -1,-1,-1
    #     if b*2 <= 200000 :
    #         print(t, "*")
    #         b1 = BFS(t+1,nextC,b*2)
    #     if b-1 >= 0 :
    #         print(t, "-")
    #         b2 = BFS(t+1,nextC,b-2)
    #     if b+1 <= 200000 :
    #         print(t, "+")
    #         b3 = BFS(t+1,nextC,b+2)
        
    #     return max(b1,b2,b3)


'''
코니는 계차수열
브라운은 +1, -1, *2 로 이동
200000 이하, 0이상인 범위에서 수행


--
11 2
5
'''
