def solution(road, n): 
    road = list(map(int, " ".join(road).split()))
    connect = []
    create_road = True  # 이전값이 0일 경우
    r = 0
    for i in range(len(road)) :
        if road[i] :
            if create_road :
                connect.append([0,0])
                create_road = False
            for j in range(r, len(connect)) :
                if connect[j][1] < n+1 :
                    connect[j][0] += 1
        else :
            connect.append([0,0])
            for j in range(r, len(connect)) :
                if connect[j][1] < n :
                    connect[j][1] += 1
                    connect[j][0] += 1
                elif connect[j][1] == n :
                    connect[j][1] += 1
                    r = j+1
                
            create_road = True

    connect.sort(reverse=True)
    return connect[0][0]

# 이게 최악인뎁
# print(solution("0"*300000,300000))

print(solution("111011110011111011111100011111",3))


"""
- dp로 풀라면 지금 인덱스, 이때까지 메꾼숫자 카운트, 지금위치에서 가장 긴 길이 3개가 같으면 dp가능함

- 시작점0으로 하고, 0 나오면 위치 push, 매꿀수 있는 갯수 초과하면, 시작점 ~ 그 위치까지 수 저장하고, pop 해서 시작점 팝한 위치+1로 바꿈

"""
