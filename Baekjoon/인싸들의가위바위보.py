"""
인싸들의 가위바위보
https://www.acmicpc.net/problem/16986
"""
def playOneGame(K,count,winner,nextPlayer) :
# K : 승률, count : 승수, winner : 이긴 사람, next : 다음 대진햣 
    player = nextPlayer.pop()
    if winner == 2 :
        # N가지를 반복해서 다음게임 진행
        pass
    elif player == 2 :
        pass
    else :
        winnerV = players[winner].pop()
        playerV = players[player].pop()

        if role[winnerV][playerV] == 0 :
            nextPlayer.append(player)
            playOneGame(K,count,winner,nextPlayer)
        else :
            nextPlayer.append(winner)
            playOneGame(K,count,player,nextPlayer)


    # k = 0
    # winner = 1
    # while queue :
    #     if k == K :
    #         break
    #     # 게임한판
    #     player = queue.pop()
    #     if winner == 1 :

    #         pass
    #     elif player ==  1 :
    #         pass
    #     else :
    #         pass




N, K = map(int, input().split())
role = [ list(map(int, input().split())) for _ in range(N)]
players = [ list(map(int, input().split())) for _ in range(2)]
visited = [ False for _ in range(N) ]