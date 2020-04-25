"""
길 찾기 게임
"""
import sys
sys.setrecursionlimit(10**6)
tree = []
r1, r2 = [], []
# 전위순회, 후위순회
def preorder_traverse(T) :
    if T :
        r1.append(T)
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])
def postorder_traverse(T) :
    if T :
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        r2.append(T)

def solution(nodeinfo):
    N = len(nodeinfo)

    for i in range(N) :
        nodeinfo[i][0], nodeinfo[i][1] = nodeinfo[i][1],nodeinfo[i][0]
        nodeinfo[i].append(i+1)
    nodeinfo.sort(reverse=True)

    global tree
    tree = [[0, 0] for _ in range(N + 1)]
    root = nodeinfo[0][2]
    # root노드에 자식 삽입
    baby = nodeinfo[1][0]
    if nodeinfo[0][1] < nodeinfo[1][1] :
        tree[root][1] = nodeinfo[1][2]
        if nodeinfo[2][0] == baby :
            tree[root][0] = nodeinfo[2][2]
            i = 3
        else :
            i = 2
    else :
        tree[root][0] = nodeinfo[1][2]
        if nodeinfo[2][0] == baby :
            tree[root][1] = nodeinfo[2][2]
            i = 3
        else :
            i = 2
    # 큐에 데이터 삽입 [인덱스, 본인x, 부모x]
    queue = []
    for k in range(1,i) :
        queue.append([nodeinfo[k][2],nodeinfo[k][1],nodeinfo[0][1]])

    while i < N :
        # [인덱스, mom x, 부모x]
        mom = queue.pop(0)
        # 할머니x보다 엄마x가 크다면,
        if mom[2] < mom[1] :
            # 본인x이 엄마x보다 크다면
            if nodeinfo[i][1] > mom[1] :
                # 엄마의 오른쪽에 삽입
                tree[mom[0]][1] = nodeinfo[i][2]
                # 본인정보 큐에 삽입
                queue.append([nodeinfo[i][2],nodeinfo[i][1],mom[1]])
                i+=1
                if i >= N : break
            # 본인이 엄마보다 작은데 할머니보단 크다면
            if nodeinfo[i][1] < mom[1] and nodeinfo[i][1] > mom[2] :
                # 엄마의 왼쪽에 삽입
                tree[mom[0]][0] =nodeinfo[i][2]
                queue.append([nodeinfo[i][2],nodeinfo[i][1],mom[1]])
                i+=1
        else :
            # 엄마보다 자식이 크고 할머니보다 작다면
            if mom[1] < nodeinfo[i][1] and nodeinfo[i][1] < mom[2] :
                # 엄마의 오른쪽에 삽입
                tree[mom[0]][1] = nodeinfo[i][2]
                # 본인 큐에 삽입
                queue.append([nodeinfo[i][2],nodeinfo[i][1], mom[1]])
                i+=1
                if i >= N: break
            # 엄마보다 자식이 작다면
            if mom[1] > nodeinfo[i][1] :
                tree[mom[0]][0] = nodeinfo[i][2]
                queue.append([nodeinfo[i][2],nodeinfo[i][1],mom[1]])
                i+=1
    global r1, r2
    r1, r2 = [], []
    preorder_traverse(root)
    postorder_traverse(root)
    answer = [r1,r2]

    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
print(solution([[6,0],[7,2],[5,1],[4,3]]))