"""
미생물격리
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl
"""
def is_boundary(x, y) :
    if x == 0 or x == N-1 :
        return True
    if y == 0 or y == N-1 :
        return True
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for test_case in range(1, 1+T) :
    N, M, K = map(int, input().split())

    queue = [0]*K
    for k in range(K) :
        x, y, n, d = map(int, input().split())
        queue[k] = [x,y,n,d-1]
    
    m = 0
    while m < M :
        # 삭제할 값
        for q in range(len(queue)) :
            if queue[q][2] :
                x, y, n, d = queue[q]
                x += dx[d]
                y += dy[d]
                
                if is_boundary(x,y) :
                    n = n//2
                    d = d-1 if d%2 else d+1
                
                queue[q] = [x, y, n, d]

        # 겹치는 위치 구하기
        for q in range(len(queue)) :
            if queue[q][2] :
                x, y, n, d = queue[q]
                total_n, max_n = n, n
                for i in range(q+1, len(queue)) :
                    if queue[i][2] and queue[i][0] == x and queue[i][1] == y :
                        total_n += queue[i][2]
                        if max_n < queue[i][2] :
                            max_n = queue[i][2]
                            d = queue[i][3]
                        queue[i][2] = 0
                queue[q][2], queue[q][3] = total_n, d
        m += 1

    result = 0
    for q in range(len(queue)) :
        result += queue[q][2]

    print('#{} {}'.format(test_case, result))

"""
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
"""