"""
1258.행렬찾기
"""
def check(x,y) :
    global n
    height, width = 0, 0

    for i in range(y,n) :
        # 벽이면 종료
        if an[x][i] == 0 :
            break
        width += 1

    for j in range(x,n) :
        if an[j][y] == 0 :
            break
        height += 1
    
    return height, width

def makeEmpty(x,y,height, width) :
    for h in range(height) :
        for w in range(width) :
            an[x+h][y+w] = 0


T = int(input())
for test_case in range(1, T+1) :
    n = int(input())
    an = [list(map(int, input().split())) for _ in range(n)]
    
    # 결과값 저장
    result = []
    num = 0
    for x in range(n) :
        for y in range(n) :
            if an[x][y] == 0 :
                continue
            
            # 다음 증가함수가 벽인지 체크
            height, width = check(x,y)
            # 행령에 저장
            num+=1
            result.append([height*width,height, width])
            # 방문한 곳 지우기
            makeEmpty(x,y,height, width)

    # 결과 정렬 함수
    result.sort()

    print(f'#{test_case} {num}', end=' ')
    for res in result :
        print(res[1], res[2], end=" ")
    print()