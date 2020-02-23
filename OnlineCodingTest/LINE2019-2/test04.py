N = int(input())
seat = list(map(int, input().strip().split(' ')))

result = 0
for i in range(N) :
    if seat[i] == 0 :
        l, r = i-1, i+1
        while l >= 0 and seat[l] == 0 : l -= 1
        while r < N and seat[r] == 0 : r += 1
        # 제일 끝 부분 비어있을 경우
        if r == N or l == -1 :
            result = max(result,max(i-l,r-i))
        else :
            result = max(result,min(i-l,r-i))
        
print(result)



# # 가장 긴 빈좌석 길이 : 20000
# longEmpty = 0
# local = 0
# for i in range(N) :
#     if seat[i] == 1 :
#         longEmpty = max(longEmpty,local)
#         local = 0
#     else :
#         local += 1
# longEmpty = max(longEmpty,local)
# # 나누기 2 
# print((longEmpty+1)//2 if longEmpty%2 else longEmpty//2)



"""
10
0 0 0 0 1 0 1 0 0 0
8
1 0 1 0 0 0 0 0
7
0 0 0 0 1 0 1
"""

