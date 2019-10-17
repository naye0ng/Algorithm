"""
차량정비소
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy&categoryId=AV6c6bgaIuoDFAXy&categoryType=CODE
"""
import collections

T = int(input())
for test_case in range(1,1+T) :
    N, M, K, A, B = map(int, input().split())
    receptionT = list(map(int, input().split()))
    repairT = list(map(int, input().split()))
    time = list(map(int, input().split()))
    # 시간 : [사람의 인덱스넣기]
    TK = {key : [] for key in range(time[-1]+1)}
    for k in range(K) :
        TK[time[k]].append(k+1)

    reception = [[0,[]] for _ in range(N)]
    repair = [[0,[]] for _ in range(M)]
    
    answer = 0
    t = 0
    end = 0
    receptionPeople, repairPeople = collections.deque([]), collections.deque([])
    while end < K :
        # [1] 수리센터 사람 내보내기
        for i in range(M) :
            if repair[i][0] == 0 :
                continue
            repair[i][0] -= 1
            if repair[i][0] == 0 :
                # 모든 수리가 끝난 사람이 지갑을 두고 간 사람인지 확인한다.
                end += 1
                if repair[i][1][1] == A and repair[i][1][2] == B :
                    answer += repair[i][1][0]
        
        # [2] 접수센터 사람 -> 수리대기인원
        for i in range(N) :
            if reception[i][0] == 0 :
                continue
            reception[i][0] -= 1
            if reception[i][0] == 0 :
                # 접수가 끝났으면, 수리 대기 인원으로 보내기
                repairPeople.append(reception[i][1])

        # [4] 수리 대기 인원을 들어온 순서대로 수리보내기
        for i in range(M) :
            # 들어갈 곳이 있다면
            if repair[i][0] == 0 and repairPeople :
                people = repairPeople.popleft()
                # 수리창구번호 입력
                people[2] = i+1
                # 수리하기
                repair[i][0] = repairT[i]
                repair[i][1] = people

        # [4] 현재 시간에 도착한 사람 -> 접수 대기 인원
        if t <= time[-1] :
            for i in TK[t] :
                receptionPeople.append([i, -1,-1])
        
        # [5] 접수 대기인원 -> 접수센터로 보내기
        for i in range(N) :
            # 들어갈 곳이 있다면
            if reception[i][0] == 0 and receptionPeople :
                people = receptionPeople.popleft()
                # 접수창구번호 입력
                people[1] = i+1
                # 접수하기
                reception[i][0] = receptionT[i]
                reception[i][1] = people
        t += 1
    if answer == 0 :
        answer = -1
    print('#{} {}'.format(test_case,answer))





"""
1
1 1 2 1 1
5
7
7 10
"""