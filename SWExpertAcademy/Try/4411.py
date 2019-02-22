 """
4411. 덕환이의 카드 뽑기
"""


# 1번 방법 : 재귀로 풀었으나, maximum recursion에러가 난다.
def cardmix(card, k) :
    # if len(card) == 1 :
    #     return card[0]   
    # elif len(card) <= k :
    #     return cardmix(card[k%len(card)+1:]+card[:k%len(card)],k)
    # else :
    #     return cardmix(card[k+1:]+card[0:k], k)





T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())

    card = [i for i in range(1,n+1)]

    print(f'#{test_case} {cardmix(card,k)}')
