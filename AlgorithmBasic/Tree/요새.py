'''
요새
https://www.algospot.com/judge/problem/read/FORTRESS
'''
def is_inside_circle(x, y, r, x2, y2) :
    if (abs(x-x2)**2 + abs(y-y2)**2) < r**2 : return True
    return False

# 이진트리가 아닌 트리 만들기
def make_tree(node, subtree) :
    parent_node = subtree[0]
    x, y, r = ramparts[parent_node]
    x2, y2, r2 = ramparts[node]

    if is_inside_circle(x, y, r, x2, y2) :
        is_descendants = False
        for i in range(1, len(subtree)) :
            if make_tree(node, subtree[i]) : 
                is_descendants = True
                break
        if not is_descendants :
            subtree.append([node])
        return True
    return False

def get_depth(subtree) :
    if len(subtree) == 1 :
        return 0

    depths = [0]
    for i in range(1, len(subtree)) :
        depths.append(get_depth(subtree[i])+1)

    # 현재 subtree에서 경로의 최대값 구하기
    if len(depths) > 1 :
        global max_depth
        max_depth = max(max_depth, sum(sorted(depths, reverse=True)[:2]))
    
    # 현재 subtree의 최대 깊이
    return max(depths)
    
T = int(input())
for _ in range(T) :
    N = int(input())
    ramparts = [list(map(int, input().split())) for _ in range(N)]

    tree = [0]
    for node in range(1, N) :
        make_tree(node, tree)

    max_depth = 0
    get_depth(tree)
    print(max_depth)

    
# 트리 모습 :[0, [1, [2, [3]], [4]], [5], [6, [7]]]
'''
[오답] 루트 노드를 방문하지 않고 서브 트리 사이에 최대 거리가 있을 수 있다.
        1
       /|
      2 3
     /|
    4 5
   /| /|
  6 7 8 9
 /   /
10   11
[루트를 걸치는 최대 거리] : 5
[서브트리 사이의 최대 거리] : 6

tree = [1,[2,[4, [6, [10]], [7]],[5, [8, [11]], [9]]],[3]]
'''