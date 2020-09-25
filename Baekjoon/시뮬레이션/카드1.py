'''
카드1
https://www.acmicpc.net/problem/2161
'''

N = int(input())
cards = [str(n+1) for n in range(N)]
answer = []
while cards :
    answer.append(cards.pop(0))
    if cards :
        cards.append(cards.pop(0))

print(" ".join(answer))