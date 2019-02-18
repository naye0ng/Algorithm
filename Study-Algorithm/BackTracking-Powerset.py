"""
DFS, Powerset 

{1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합을 구하시오
"""
def backtrack(a,k,sum) :
    c = [True, False]

    # 마지막 노드까지 도착한 경우
    if k == 10 :
        if sum == 10 :
            for i in range(1, 11) :
                if a[i] == 1 :
                    print(i, end=' ')
            print()
    else :
        k+=1
        if sum + k <= 10 :
            # 합이 10이하 일때만 본인을 선택한다.
            a[k] = 1
            backtrack(a,k,sum+k)
        a[k] = 0; backtrack(a,k,sum)

# 공집합은 항상 포함
maxcandidates = 11
nmax = 11

a = [0]*nmax

backtrack(a,0,0)



"""
불필요한 연산 처리 안한 부분
"""
# def backtrack(a,k,end) :
#     c = [True, False]

#     # 마지막 노드까지 도착한 경우, 원하는 연산 수행
#     if k == end :
#         issumofset10(a)
#     else :
#         k+=1
#         for i in range(len(c)) :
#             a[k] = c[i]
#             backtrack(a,k,end)

# def issumofset10(a) :
#     sums = 0
#     sets = []
#     for i in range(len(a)):
#         if a[i] == True :
#             sums+=i
#             sets+=[i]
    
#     if sums == 10 :
#         print(sets)


# # 공집합은 항상 포함
# maxcandidates = 11
# nmax = 11

# a = [0]*nmax

# backtrack(a,0,10)