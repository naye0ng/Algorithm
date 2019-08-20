"""
열쇠
https://www.acmicpc.net/problem/9328
"""

# BFS
# 오, 왼, 위, 아래
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def isNotWall(x,y,h,w) :
    if x > 0 and x < h-1 :
        if y > 0 and y < w-1 :
            if arr[x][y] != '*' and arr[x][y] != 0:
                return True
    return False

def getKeys(h,w) :
    queue = []
    # 벽이 아닌 입구를 모두 찾기
    for x in range(h) :
        if x == 0 or x == h-1 :
            for y in range(w) :
                if arr[x][y] != '*':
                    queue.append([x,y])      
        else :
            if arr[x][0] != '*' :
                queue.append([x,0])                      
            elif arr[x][w-1] != '*' :
                queue.append([x,w-1]) 
    
    docs = 0
    # TODO: 키를 새로 수집하기
    while queue :
        q = queue.pop()
        x, y = q[0], q[1] 
        # 여기서 검사해서 넘김
        if arr[x][y] == '$' :
            docs+= 1
            arr[x][y] = 0
        elif arr[x][y] == '.' :
            arr[x][y] = 0
        # 대문자
        elif ord(arr[x][y]) >= 65 and ord(arr[x][y]) <= 90 :
            # 키가 존재하면 열기
            if chr(ord(arr[x][y])+32) in keys :
                arr[x][y] = 0
            # 키가 존재하지 않는 경우에 대한 무언가
        # 소문자
        elif ord(arr[x][y]) >= 97 and ord(arr[x][y]) <= 122 :
            keys.append([x,y])
            arr[x][y] = 0

        # 더 갈수 있는 장소 찾기
        if arr[x][y] == 0 :
            for i in range(4) :
                if isNotWall(x+dx[i],y+dy[i],h,w) :
                    queue.append([x+dx[i],y+dy[i]])

    return docs
                     


T = int(input())
for _ in range(T) :
    h, w = map(int,input().split())
    arr = [ " ".join(input()).split() for _ in range(h)]
    keys = " ".join(input()).split()
    print(getKeys(h,w))
    print(arr)