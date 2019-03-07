"""
1979.어디에 단어가 들어갈 수 있을까

- 1 : 숫자 3을 이용하여 방향성 체크 아이디어!(박수!!)
- 2 :인풋데이터에 빈 배열을 넣어 각 함수를 간소화 함
"""

# (2)
def right(x,y) :
    if blanks[x][y+1] != 0 :
        # 오른쪽으로 이동했음을 체크
        blanks[x][y+1] -= 1
        return 1 + right(x,y+1)
    return 1

def down(x,y) :
    if blanks[x+1][y] != 0 :
        # 아래쪽으로 이동했음을 체크
        blanks[x+1][y] -= 2
        return 1 + down(x+1,y)
    return 1

T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    # 맨 오른쪽, 맨 뒤에 빈칸 삽입
    blanks = [ [3 if i == 1 else i for i in list(map(int, input().split()))]+[0] for _ in range(N)]+[[0]*(N+1)]

    result = 0
    for x in range(N) :
        for y in range(N) :
            if blanks[x][y] == 2 :
                d = down(x,y)
                if d == K :
                    result+=1
            elif blanks[x][y] == 1 :
                r = right(x,y)
                if r == K :
                    result+=1
            elif blanks[x][y] == 3 :
                d = down(x,y)
                r = right(x,y)
                if d == K :
                    result+=1
                if r == K :
                    result+=1

    print('#{} {}'.format(test_case, result))


# (1)
# # 아래로
# def down(x,y,length) :
#     # 갈 곳이 있다면
#     if x+1 != n and blanks[x+1][y] !=0 :
#         # 지나왔음을 마킹
#         blanks[x+1][y] -=1
#         length += 1
#         return down(x+1,y,length)
#     return length
# 
# # 오른쪽으로 
# def right(x,y,length) :
#     # 갈 곳이 있다면
#     if y+1 != n and blanks[x][y+1] !=0 :
#         # 지나왔음을 마킹
#         blanks[x][y+1] -=2
#         length += 1
#         return right(x,y+1,length)
#     return length
# 
# T = int(input())
# for test_case in range(1, T+1) :
#     n, k = map(int,input().split())
#     blanks = [ [ 3 if i==1  else i for i in map(int,input().split()) ] for _ in range(n)]
#     numBlank = {i:0 for i in range(1,n+1)}
#   
#     for x in range(n) :
#         for y in range(n) :
#             if blanks[x][y] == 0 :
#                 continue
#             if blanks[x][y] == 3 :
#                 numBlank[down(x,y,1)] +=1
#                 numBlank[right(x,y,1)] +=1
#             elif blanks[x][y] == 2 :
#                 numBlank[right(x,y,1)] +=1
#             elif blanks[x][y] == 1 :
#                 numBlank[down(x,y,1)] +=1
# 
# 
#     print(f'#{test_case} {numBlank[k]}')