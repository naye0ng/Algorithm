"""
라면공장
"""
# global answer
# answer = 0

# def getSuppliesDay(stock, dates, supplies,visited, k, before, choose) :
#     global answer
#     if dates[before] + stock >= k :
#         print("완료")
#         if answer == 0 or answer > choose :
#             answer = choose
#     else :
#         for d in range(len(dates)) :
#             if d <= before :
#                 continue
#             if dates[d] <= dates[before] + stock and not visited[d] :
#                 visited[d] = True
#                 print(dates[d], "선택 -번째?",choose+1)
#                 getSuppliesDay(stock-dates[d]+supplies[d], dates, supplies,visited, k, d, choose+1)
#                 visited[d] = False

# def solution(stock, dates, supplies, k):
#     global answer
#     visited = [False]*len(dates)

#     # 공급가능 첫날 찾기
#     for d in range(len(dates)) :
#         if dates[d] > stock :
#             break
#         print(dates[d], "시작======")
#         visited[d] = True
#         getSuppliesDay(stock-dates[d]+supplies[d], dates, supplies,visited, k, d, answer+1)
#         visited[d] = False

#     return answer

global answer

def getPath(stock, dates, supplies, k, visited, before, count) :
    global answer
    if stock >= k :
        if answer == 0 or answer > count :
            answer = count
    else :
        for d in range(before+1, len(dates)) :
            # 방문한 적이 없고 만약 전체 stock보다 이전의 날짜인 경우에만
            if not visited[d] and dates[d] <= stock :
                if answer == 0 or count < answer :
                    visited[d] = True
                    getPath(stock+supplies[d], dates, supplies, k, visited,d,count+1)
                    visited[d] = False

def solution(stock, dates, supplies, k):
    global answer
    answer = 0

    visited = [False]*len(dates)
    for d in range(len(dates)) :
        if dates[d] <= k :
            visited[d] = True
            getPath(stock+supplies[d], dates, supplies, k, visited,d,1)
            visited[d] = False        
    return answer



print(solution(10, [5, 10, 12, 15, 20], [5, 10,5,10,80], 100))
