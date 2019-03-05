"""
1798.범준이의 제주도 여행 계획
"""
def plan(day) :
    # 나는 아직 멀었다.....
    pass

T = int(input())
for test_case in range(1,T+1) :
    n, m = map(int, input().split())
    path = []

    # 경로번호로 바로 접근하기 위해 바꿔줌
    for i in range(1,n) :
        path.append([0]*i+list(map(int, input().split())))

    numP = 0
    nodes = [ input().split() for _ in range(n) ]
    for node in nodes :
        if len(node) == 3 :
            # p의 인덱스는 1 ~ numP까지가 된다.
            numP += 1
            node[1] = int(node[1])
            node[2] = int(node[2])

    visitied = [0]*n


    print(f'#{test_case} ')