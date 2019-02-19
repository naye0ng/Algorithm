"""
4880.토너먼트 카드게임
"""
def cardGames(s,l) :
    if s == l :
        return personCards[s-1]
    else :
        p1 = cardGames(s, (s+l)//2)
        p2 = cardGames((s+l)//2+1,l)
        if abs(p1[1]-p2[1]) == 1:
            if p1[1] > p2[1] :
                return p1
            return p2
        elif abs(p1[1]-p2[1]) == 2:
            if p1[1] > p2[1] :
                return p2
            return p1
        else :
            # 비기는 경우
            return p1


T = int(input())
for test_case in range(1,T+1) :
    n = int(input())
    cards = list(map(int,input().split()))

    personCards = [[i+1,cards[i]] for i in range(len(cards))]

    winner = cardGames(1, n)
    print(f'#{test_case} {winner[0]}')