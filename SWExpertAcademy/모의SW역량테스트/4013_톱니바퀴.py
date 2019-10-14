"""
톱니바퀴
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&categoryId=AWIeV9sKkcoDFAVH&categoryType=CODE
"""

def clockwise(i) :
    temp = wheel[i][-1]
    for k in range(8) :
        temp, wheel[i][k] = wheel[i][k], temp

def counterclockwise(i) :
    temp = wheel[i][0]
    for k in range(7,-1,-1) :
        temp, wheel[i][k] = wheel[i][k], temp

def cycle(i, d, s) :
    left, right = wheel[i][-2], wheel[i][2]
    
    if d == 1 :
        clockwise(i)
    elif d == -1 :
        counterclockwise(i)
    # left
    if s <= 0 and i-1 >= 0 and wheel[i-1][2] != left :
        cycle(i-1,d*(-1),-1)
    # right
    if s >= 0 and i+1 < 4 and wheel[i+1][-2] != right :
        cycle(i+1,d*(-1),1)

T = int(input())
for test_case in range(1,T+1) :
    K = int(input())
    wheel = []
    for _ in range(4) :
        wheel.append(list(map(int, input().split())))

    for _ in range(K) :
        i, d = map(int, input().split())
        cycle(i-1, d, 0)
       
    score = 0
    for i in range(4) :
        if wheel[i][0] :
            score += 2**(i)
        
    print('#{} {}'.format(test_case,score))


"""
1
2
1 0 0 1 0 0 0 0
0 1 1 1 1 1 1 1
0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1
3 1
1 1

14
"""