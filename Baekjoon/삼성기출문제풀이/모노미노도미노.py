"""
모노미노도미노
https://www.acmicpc.net/problem/19235
"""

def drop(arr) :
    for x in range(4, -1, -1) :
        for y in range(4) :
            if arr[x][y] == 1 or arr[x][y] == 3:
                for k in range(x+1, 6) :
                    if arr[k][y] != 0 : break
                    arr[k-1][y], arr[k][y] = arr[k][y], arr[k-1][y]
            # 안떨어진 2번블록의 두번째 부분 체크
            if y+1 < 4 and arr[x][y] == 2 and arr[x][y+1] == 2:
                for k in range(x+1, 6) :
                    if arr[k][y] != 0 or arr[k][y+1] != 0 : break
                    arr[k-1][y], arr[k][y] = arr[k][y], arr[k-1][y]
                    arr[k-1][y+1], arr[k][y+1] = arr[k][y+1], arr[k-1][y+1]

def arr_pop_insert(arr, x) :
    arr.pop(x)
    arr.insert(0, [0]*4)

def bomb(arr) :
    global score

    need_drop = True
    while need_drop :
        need_drop = False
        # 동일한 시기에 꽉찬 부분 한번에 삭제
        for x in range(6) :
            if 0 not in arr[x] : 
                score += 1
                arr_pop_insert(arr, x)
                need_drop = True
        drop(arr)
                
    if sum(arr[0]) : 
        arr_pop_insert(arr, -1)
    if sum(arr[1]) :
        arr_pop_insert(arr, -1)
    
def block_01(arr, x, y) :
    for i in range(6) :
        if i+1 == 6 or arr[i+1][y] : 
            arr[i][y] = 1
            break
    bomb(arr)

def block_02(arr, x, y) :
    for i in range(6) :
        if i+1 == 6 or arr[i+1][y] or arr[i+1][y+1] :
            arr[i][y] = arr[i][y+1] = 2
            break
    bomb(arr)

def block_03(arr, x, y) :
    for i in range(6) :
        if i+1 == 6 or arr[i+1][y] : 
            arr[i][y] = arr[i-1][y] = 3
            break
    bomb(arr)

score = 0
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]

N = int(input())
for _ in range(N) :
    t, x, y = map(int, input().split())

    if t == 1 :
        block_01(green, x, y)
        block_01(blue, y, x)
    elif t == 2 :
        block_02(green, x, y)
        block_03(blue, y, x)
    else :
        block_03(green, x, y)
        block_02(blue, y, x)

blocks = 0
for x in range(6) :
    for y in range(4) :
        if green[x][y] : blocks += 1
        if blue[x][y] : blocks += 1

print(score)
print(blocks)