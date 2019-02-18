"""
DFS구현2 : 재귀로 구현
"""
def DFS(v) :
    print(v)
    visitied[v] = True 

    for i in range(1,8):
        if G[v][i] and not visitied[i] :
            DFS(i)

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visitied = [0]*8

# G는 연관성
G = [[0]*8 for _ in range(8)]