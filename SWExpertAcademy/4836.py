"""
4836.색칠하기
"""
T = int(input())

for test_case in range(1, T + 1):

    an = [[0]*10 for i in range(10)]

    for n in range(int(input())) :
        x1,y1,x2,y2,color = map(int,input().split())
        for i in range(x1,x2+1) :
            for j in range(y1,y2+1) :
                an[i][j] +=color

    # 보라색 찾기
    count = 0
    for i in range(0,10) :
        for j in range(0,10) :
            if an[i][j] == 3 :
                count+=1
    
    print(f'#{test_case} {count}')

