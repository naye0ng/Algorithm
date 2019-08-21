"""
열쇠
https://www.acmicpc.net/problem/9328
"""
import sys
sys.stdin = open('input.txt','r')

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
    notOpenDoor = {}
    while queue :
        q = queue.pop(0)
        x, y = q[0], q[1] 
        # 여기서 검사해서 넘김
        if arr[x][y] != 0 :
            if arr[x][y] == '$' :
                docs += 1
                arr[x][y] = 0
            elif arr[x][y] == '.' :
                arr[x][y] = 0
            # 대문자
            elif ord(arr[x][y]) >= 65 and ord(arr[x][y]) <= 90 :
                # 키가 존재하면 열기
                if chr(ord(arr[x][y])+32) in keys :
                    arr[x][y] = 0
                # 열지 못한 문에 대한 키를 따로 가지고 있자
                elif chr(ord(arr[x][y])+32) in notOpenDoor :
                    notOpenDoor[chr(ord(arr[x][y])+32)].append([x,y])
                else :
                    notOpenDoor[chr(ord(arr[x][y])+32)] = []
                    notOpenDoor[chr(ord(arr[x][y])+32)].append([x,y])
            elif ord(arr[x][y]) >= 97 and ord(arr[x][y]) <= 122 :
                keys.append(arr[x][y])
                # [이부분이 핵심]열수 있는 키가 있다면 문들 추가
                if arr[x][y] in notOpenDoor :
                    queue.extend(notOpenDoor[arr[x][y]])
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
