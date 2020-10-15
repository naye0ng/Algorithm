'''
무선충전
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE
'''

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]
def is_not_wall(x, y) :
    if x < 0 or x >= 11 : return False
    if y < 0 or y >= 11 : return False
    return True

# [100, 80], [100, 20]인 경우에 100과 20을 선택하는 경우가 생기므로 두 배열 조합의 최대값을 구하자
def get_battery(x1, y1, x2, y2) :
    battery = 0
    for i1 in board[x1][y1] :
        for i2 in board[x2][y2] :
            if i1 == i2 : 
                battery = max(battery, BC[i1])
            else :
                battery = max(battery, BC[i1]+BC[i2])
    return battery

T = int(input())
for test_case in range(1, 1+T) :
    M, A = map(int, input().split())
    move1 = list(map(int, input().split()))
    move2 = list(map(int, input().split()))

    board = [[[A] for i in range(11)] for _ in range(11)]
    BC = [0]*(A+1)
    BC[A] = 0
    for bc in range(A) :
        visited = [[False]*11 for _ in range(11)]
        x, y, c, p = map(int, input().split())
        BC[bc] = p
        board[x][y].append(bc)
        visited[x][y] = True
        queue = [[x, y]]
        while c :
            for i in range(len(queue)) :
                x, y = queue.pop(0)
                for d in range(1, 5) :
                    if is_not_wall(x+dx[d], y+dy[d]) and not visited[x+dx[d]][y+dy[d]] :
                        board[x+dx[d]][y+dy[d]].append(bc)
                        visited[x+dx[d]][y+dy[d]] = True
                        queue.append([x+dx[d], y+dy[d]])
            c -= 1
    
    x1, y1, x2, y2 = 1, 1, 10, 10
    charged_battery = get_battery(x1, y1, x2, y2)
    for m in range(M) :
        x1 += dx[move1[m]]
        y1 += dy[move1[m]]
        x2 += dx[move2[m]]
        y2 += dy[move2[m]]

        charged_battery += get_battery(x1, y1, x2, y2)
        
    print('#{} {}'.format(test_case, charged_battery))
