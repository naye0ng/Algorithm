""""
10158.개미

- 시도1 : 불필요한 이동 횟수를 maxShift로 제어하면서 회전을 찾음 >> 런타임 에러
- 시도2 : x, y를 모듈러 연산을 통해 회전을 제거하고 maxShift로 불필요한 연산을 줄임,
          이 경우 모든 회전을 제거하였으므로 while루프는 최대 2번 돈다.
"""

W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())
dx, dy = 1, 1

xt = T%(2*W)
while xt!=0 :
    maxShift = 1
    if p == 0 or p == W :
        dx = dx*(-1)
    # 이 방향으로 최대 이동할 수 있는 값
    if dx == 1 :
        maxShift = W-p
    elif dx == -1 :
        maxShift = p

    if xt < maxShift:
        maxShift = xt

    p = p+(dx*maxShift)
    xt -= maxShift

yt = T%(2*H)
while yt!=0 :
    maxShift = 1
    if q == 0 or q == H :
        dy = dy*(-1)
    # 이 방향으로 최대 이동할 수 있는 값
    if dy == 1 :
        maxShift = H-q
    elif dy == -1 :
        maxShift = q

    if yt < maxShift:
        maxShift = yt

    q = q+(dy*maxShift)
    yt -= maxShift

print('{} {}'.format(p,q))


# t = T
# dx, dy = 1, 1
# initX, initY = p, q
#
# while t != 0 :
#     maxShift = 1
#     if p == 0 or p == W :
#         dx = dx*(-1)
#     if q == 0 or q == H :
#         dy = dy*(-1)
#     # 이 방향으로 최대 이동할 수 있는 값
#     if dx == 1 :
#         maxShift = W-p
#     elif dx == -1 :
#         maxShift = p
#
#     if dy == 1 :
#         if maxShift > H-q :
#             maxShift = H-q
#     elif dy == -1 :
#         if maxShift > q :
#             maxShift = q
#
#     if t < maxShift :
# #         maxShift = 1
#
#     p = p+(dx*maxShift)
#     q = q+(dy*maxShift)
#
#     t -= maxShift
#
#     # 회전 찾기, T-t만큼 회전
#     if initX == p and initY == q :
#         t = T%(T-t)
#
# print(p, q)

# # 회전 찾기
# initX, initY = p, q
# circle = [[p,q]]
# check = 0
#
# for _ in range(t) :
#     if p == 0 or p == W :
#         dx = dx*(-1)
#     if q == 0 or q == H :
#         dy = dy*(-1)
#
#     p = p+dx
#     q = q+dy
#     if p == initX and q == initY :
#         check = 1
#         break
#     circle.append([p,q])
#
# if check != 0 :
#     i = t%len(circle)
#     p = circle[i][0]
#     p = circle[i][1]

