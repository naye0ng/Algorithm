"""
BFS.깊이우선탐색
"""
def visit(t) :
    pass


def BFS(G, v) :
    global n
    # 방문 확인
    visitied = { i:0 for i in range(1,n+1)}

    queue = []
    # 정점 v부터 탐색 시작
    queue.append(v)

    while queue :
        t= queue.pop(0)
        if not visitied[t] :
            visitied[t] = True
            
            # 원하는 연산 
            print("방문 완료",t)
            visit(t)
        
        for i in G[t-1] :
            if not visitied[i] :
                queue.append(i)


n = 9
G = [[2,3,4],[5,6],[8],[7,8,9],[],[],[],[],[]]

BFS(G, 1)

# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
