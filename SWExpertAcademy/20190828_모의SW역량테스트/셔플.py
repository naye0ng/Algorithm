import copy

# 정렬조회
def checkOrderUp(N,cards):
    for i in range(1,N+1) :
        if cards[i-1] != i :
            return False
    return True

def checkOrderDown(N,cards):
    for i in range(N,0,-1) :
        if cards[N-i] != i :
            return False
    return True

def shuffle(N, depth, cards) :
    if depth <= 5 :
        global result
        if checkOrderUp(N,cards) or checkOrderDown(N,cards):
            result = min(depth,result)
        # 머지소트
        for x in range(1,N) :
            if x > N//2 :
                x = N-x
            start = N//2-x
            end = start+(2*x)
            for i in range(start,end,2) :
                cards[i], cards[i+1] = cards[i+1], cards[i]
            if checkOrderUp(N, cards) or checkOrderDown(N, cards):
                result = min(depth+1, result)
                break
            shuffle(N,depth+1,copy.deepcopy(cards))

T = int(input())
for test_case in range(1, T+1) :
    result = 6
    N = int(input())
    cards = list(map(int,input().split()))
    shuffle(N, 0, cards)
    if result == 6 :
        result = -1
    print('#{} {}'.format(test_case, result))