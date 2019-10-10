"""
로봇 청소기
https://www.acmicpc.net/problem/14503
"""
def isNotWall(x,y) :
    global N, M
    if x < 0 or x >= N :
        return False
    if y < 0 or y >= M :
        return False
    return True

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
x, y, d = map(int, input().split())

board = [ list(map(int, input().split())) for _ in range(N)]

result = 0
clean = True
while True :
    # 현재 위치 청소
    if clean :
        board[x][y] = 2
        result += 1
        clean = False

    cnt = 0
    while cnt < 4 :
        # [오류!!!] d-1의 경우 음수가 나오므로 양수를 만든뒤에 모듈러 연산
        d2 = (d+3)%4
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if isNotWall(x+dx[d2],y+dy[d2]) and board[x+dx[d2]][y+dy[d2]] == 0 :
            d = d2
            x += dx[d]
            y += dy[d]
            clean = True
            break
        else :
            # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            d = d2
            cnt += 1
            
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 
    if cnt == 4 :
        # [후진] 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        d2 = (d+2)%4
        x += dx[d2]
        y += dy[d2]
        # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        if not isNotWall(x,y) or board[x][y] == 1:
            break

print(result)

"""
5 5
2 2 0
1 1 1 1 1 
1 0 0 1 1 
1 0 0 0 1 
1 0 0 0 1 
1 1 1 1 1
"""