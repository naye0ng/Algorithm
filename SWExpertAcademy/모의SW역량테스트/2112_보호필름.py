"""
보호필름
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
def check() :
    global D, W, K 
    for y in range(W) :
        # 한줄씩 체크
        cnt, stop = 0, True
        for x in range(1, D) :
            a, b = 0, 0
            if visited[x-1] == -1 :
                a = layer[x-1][y]
            elif visited[x-1] == 0 :
                a = 0
            elif visited[x-1] == 1 :
                a = 1
            if visited[x] == -1 :
                b = layer[x][y]
            elif visited[x] == 0 :
                b = 0
            elif visited[x] == 1 :
                b = 1
            if b == a :
                cnt += 1
                if cnt >= K-1 :
                    stop = False
                    break
            else :
                cnt = 0
        if stop :
            return False
    return True

# 약품 한개를 선택할 때마다 A, B약품을 처리해서 넘기자.
def medical(n, k) :
    global result
    if k <= result :
        if n == D :
            # visited 체크하기
            if check():
                result = k
        elif n < D :
            visited[n] = -1
            medical(n+1,k)

            visited[n] = 0
            medical(n+1,k+1)
        
            visited[n] = 1
            medical(n+1,k+1)
    
T = int(input())
for test_case in range(1,1+T):
    D, W, K = map(int, input().split())
    layer = [ list(map(int, input().split())) for _ in range(D)]
    visited = [-1]*D
    result = D
    if K == 1 :
        result = 0
    else :
        medical(0,0)
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
"""