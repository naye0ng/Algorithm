"""
1486. 장훈이의 높은 선반
"""
import sys
sys.stdin = open('input.txt','r')

def top(next,s) :
    if B <= s :
        global minH
        if s < minH :
            minH = s
    elif next < N :
        top(next+1,s+h[next])
        top(next+1,s)

T = int(input())
for test_case in range(1,1+T) :
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    minH = sum(h)
    top(0,0)

    print('#{} {}'.format(test_case, minH-B))


# def dfs(idx, cum_h):
#     if cum_h >= B:
#         global min_res
#         if cum_h <= min_res:
#             min_res = cum_h
#     elif idx < N:
#         dfs(idx + 1, cum_h)
#         dfs(idx + 1, cum_h + heights[idx])
#
#
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     heights = list(map(int, input().split()))
#     min_res = sum(heights)
#     dfs(0, 0)
#     print(f"#{tc} {min_res-B}")