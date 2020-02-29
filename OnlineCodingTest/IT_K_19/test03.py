import re, copy

candidate = []
resultList = []
def makeBannedList(N,n,candi) :
    if N == n :
        global resultList
        notAready = True
        for result in resultList :
            if result == candi :
                notAready = False 
                break
        if notAready :
            resultList.append(copy.deepcopy(candi))
    else :
        # 하나씩 뽑을 것임
        for user in candidate[n] :
            if user not in candi :
                candi.add(user) 
                makeBannedList(N, n+1, candi)
                candi.remove(user)

def solution(user_id, banned_id):
    global candidate, resultList
    N = len(banned_id)
    candidate = [[] for _ in range(N)]
    for i in range(N):
        banned = ".".join(banned_id[i].split("*"))
        regex = re.compile(banned)
        
        for user in user_id : 
            if len(user) == len(banned) and regex.search(user) :
                # 비교 했으면 가능한 값을 저장하기
                candidate[i].append(user)

    # 후보를 정했으면 매칭
    makeBannedList(N,0,set([]))
    return len(resultList)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))