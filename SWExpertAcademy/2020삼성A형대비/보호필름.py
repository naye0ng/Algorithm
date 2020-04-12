"""
보호필름
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
"""
def is_pass() :
    for y in range(W):
        is_not_pass = True
        before, cnt = -1,0
        for x in range(D) :
            if before != cell[x][y] :
                before = cell[x][y]
                cnt = 1
            else :
                cnt += 1
                if cnt >= K :
                    is_not_pass = False
                    break
        # 하나라도 부적격이면 통과 못함
        if is_not_pass :
            return False
    return True

# 시약 떨어뜨릴 위치 찾기
def change_cell(n, k) :
    global result
    if is_pass() :
        result = min(result, n)
    elif n < result :
        for m in range(k, D) :
            tmp = cell[m]
            cell[m] = [0]*W
            change_cell(n+1, m+1)
            cell[m] = [1]*W
            change_cell(n+1, m+1)
            cell[m] = tmp
            

T = int(input())
for test_case in range(1, 1+T) :
    D, W, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(D)]
    result = K
    change_cell(0, 0)
    print('#{} {}'.format(test_case, result))

"""
1
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1

1
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 0 0 0 0 1
1 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
"""